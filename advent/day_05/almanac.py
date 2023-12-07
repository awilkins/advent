from __future__ import annotations

from collections import namedtuple
from itertools import chain, batched
from multiprocessing import Pool

from advent.util import get_resource_lines

from typing import Sequence, List, Tuple, NamedTuple, Iterable

class MapLine(NamedTuple):
    dest: int
    source: int
    range: int

class Mapping(NamedTuple):
    name: str
    map: List[MapLine]

class Almanac:

    seeds: List[int]
    maps: List[Mapping]

    def __init__(self, lines: Sequence[str]):

        # first line is seeds
        self.seeds = [int(s) for s in lines[0].split(':')[1].split()]

        the_rest = iter(lines[2:])

        maps = []

        while line := next(the_rest, None):

            map_name = line.split()[0]
            new_map = []

            while line := next(the_rest, None):
                if not line[0].isdigit():
                    continue
                new_map.append(MapLine(
                    *(int(l) for l in line.split())
                ))

            maps.append(Mapping(
                map_name, sorted(new_map)
            ))

        self.maps = maps

    def map_location(self, seed: int):

        for map in self.maps:
            for map_line in map[1]:
                dest, source, range = map_line

                if source <= seed <= (source + range - 1):
                    offset = dest - source
                    seed += offset
                    break

        return seed


def answer_1(lines: Sequence[str]):
    al = Almanac(lines)
    return min(
        [al.map_location(seed) for seed in al.seeds]
    )

def batch(args):
    lines, start, count = args
    al = Almanac(lines)
    seeds = range(start, start + count)
    return min(al.map_location(seed) for seed in seeds)

JOB_SIZE = 10_000_000
def job_generator(batches):

    for start, count in batches:
        low_water = start
        while low_water + JOB_SIZE < start + count:
            print(f"Job : {low_water} -> {low_water + JOB_SIZE}")
            yield low_water, JOB_SIZE
            low_water += JOB_SIZE
        print(f"Job : {low_water} -> {low_water + JOB_SIZE}")
        yield low_water, (start + count - low_water)


def answer_2(lines: Sequence[str]):
    al = Almanac(lines)

    print(f"Batch sizes : {[r for s, r in batched(al.seeds, 2)]}")
    total_seeds = sum(r for s, r in batched(al.seeds, 2))

    print(f"\nTotal Seeds : {total_seeds}")

    jobs = job_generator(batched(al.seeds, 2))

    with Pool(16) as p:
        return min(p.map(batch, [(lines, start, count) for start, count in jobs]))

def answer_2_smart(lines: Sequence[str]):
    al = Almanac(lines)

    def smallest_source(map: Mapping):
        return min(
            line.source for line in map.map
        )

    t_start, t_end = 0, smallest_source(al.maps[-1])
    target_ranges = [(t_start, t_end)]

    def can_hit(line: MapLine, range):
        t_start, t_end = range
        l_start, l_end = line.dest, line.dest + line.range

        return t_start <= l_start <= t_end or \
               t_start <=  l_end  <= t_end or \
               l_start <= t_start and t_end <= l_end

    viable_maplines = []
    for map in al.maps[-2::-1]:

        viable_maplines = [
            line for line in map.map if
            any(
                can_hit(line, trange) for trange in target_ranges
            )
        ]
        target_ranges = [
            (line.source, line.source + line.range) for line in viable_maplines
        ]
        print(len(target_ranges))

    return len(viable_maplines)




if __name__ == "__main__":
    lines = get_resource_lines("05")
    print(answer_2(lines))


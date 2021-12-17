
from itertools import count, product
from typing import List, Tuple


Velocity = Tuple[int, int]
Position = Tuple[int, int]
Box = Tuple[Position, Position]


def step(p: Position, v: Velocity) -> Tuple[Position, Velocity]:
    px, py = p
    vx, vy = v

    rp = (px + vx, py + vy)

    rvx = vx - 1
    rvx = max(rvx, 0)

    rvy = vy - 1
    rv = (rvx, rvy)

    return rp, rv


def hit_or_miss(iv: Velocity, target: Box) -> Tuple[bool, List[Position]]:
    ip = (0, 0)

    cp = ip
    cv = iv

    cpx, cpy = ip

    (nearx, topy), (farx, bottomy) = target

    trajectory: List[Position] = [
        ip
    ]

    while cpx < farx and cpy > bottomy:
        cp, cv = step(cp, cv)
        trajectory.append(cp)
        cpx, cpy = cp
        if  cpx >= nearx and cpx <= farx and \
            cpy <= topy  and cpy >= bottomy:
            return True, trajectory

    return False, trajectory


def parse_target(line: str) -> Box:
    coords = line.split(':')[1].strip()
    xcoord, ycoord = [c.strip() for c in coords.split(',')]
    nearx, farx = [int(x) for x in xcoord[2:].split('..')]
    bottomy, topy = [int(y) for y in ycoord[2:].split('..')]
    return (
        (nearx, topy),
        (farx, bottomy),
    )


def answer_1(lines: List[str]) -> Tuple[int, int]:

    target = parse_target(lines[0])

    # find a value for x that always lands in box
    (near_x, top_y), (far_x, bottom_y) = target
    def series(n: int): return (n * (n + 1)) // 2
    ivx = next(n for n in count() if series(n) >= near_x and series(n) <= far_x)

    previous_vy = 0
    current_vy = 0
    hit = False

    t = []
    while not hit:
        iv = (ivx, current_vy)
        hit, t = hit_or_miss(iv, target)
        previous_vy = current_vy
        current_vy += 1

    low_vy = previous_vy
    high_vy = low_vy
    high_t = t
    for current_vy in range(current_vy, current_vy + 1000):
        iv = (ivx, current_vy)
        hit, t = hit_or_miss(iv, target)
        if hit:
            high_vy = current_vy
            high_t = t
        current_vy += 1

    return high_vy, max(y for x, y in high_t)


def answer_2(lines: List[str]):


    target = parse_target(lines[0])

    # find ranges
    (near_x, _), (far_x, bottom_y) = target
    def series(n: int): return (n * (n + 1)) // 2
    min_x = next(n for n in count() if series(n) >= near_x and series(n) <= far_x)
    high_vy, _ = answer_1(lines)

    range_x = range(min_x, far_x + 1)
    range_y = range(bottom_y, high_vy + 1)

    total = 0
    sv = []
    for iv in product(range_x, range_y):
        hit, t = hit_or_miss(iv, target)
        if hit:
            total += 1
            sv.append(iv)

    return total, sv

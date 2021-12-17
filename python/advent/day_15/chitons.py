
import heapq
from itertools import product
from typing import Dict, List, Tuple
import sys

from tests.util import get_resource

Grid = List[List[int]]

def make_grid(lines: List[str]) -> Grid:
    return [
        [ int(c) for c in line ]
        for line in lines
    ]

Point = Tuple[int, int]

class CaveGraph:

    _nodes: List[Point]
    _graph: Dict[Point, Dict[Point, int]]

    def __init__(self, grid: Grid):

        self._nodes = list(
            product(
                range(len(grid)),
                range(len(grid)),
            )
        )
        self._graph = self.construct_graph(grid)


    def construct_graph(self, grid: Grid):
        graph = {}
        for node in self._nodes:
            graph[node] = {}

        for node in graph.keys():
            nx, ny = node
            edges = [ (x, y) for x, y in [
                (nx + 1, ny),
                (nx, ny + 1),
                (nx - 1, ny),
                (nx, ny - 1),
            ] if x >= 0 and x < len(grid) and y >= 0 and y < len(grid) ]
            for edge in edges:
                ex, ey = edge
                graph[node][edge] = grid[ey][ex]

        return graph


    @property
    def nodes(self):
        return self._nodes


    def outward_edges(self, node):
        return self._graph[node].keys()


    def value(self, start, end) -> int:
        return self._graph[start][end]


def dijkstra(graph: CaveGraph, start: Point):
    unvisited = []

    short_path = { node: sys.maxsize for node in graph.nodes }
    short_path[start] = 0

    heapq.heappush(unvisited, (0, start))

    previous_nodes = {}

    while unvisited:
        distance, current_min_node = heapq.heappop(unvisited)

        assert current_min_node is not None

        neighbours = graph.outward_edges(current_min_node)
        for n in neighbours:
            maybe_length = distance + graph.value(current_min_node, n)
            if maybe_length < short_path[n]:
                short_path[n] = maybe_length
                previous_nodes[n] = current_min_node
                heapq.heappush(unvisited, (maybe_length, n))

    return short_path

def solve_grid(grid: Grid) -> int:
    graph = CaveGraph(grid)

    shortness = dijkstra(graph, (0, 0))
    end = (len(grid) - 1, len(grid) - 1)

    return shortness[end]

def answer_1(lines: List[str]) -> int:
    grid = make_grid(lines)
    return solve_grid(grid)


def answer_2(lines: List[str]) -> int:

    grid = make_grid(lines)

    def wrapcrement(i: int) -> int: return i + 1 if i < 9 else 1

    big_grid_x = grid
    for _ in range(4):
        big_grid_x = [
            row + [ wrapcrement(x) for x in big_grid_x[y] ] for y, row in enumerate(grid)
        ]

    big_grid_y = big_grid_x
    for _ in range(4):
        big_grid_y = big_grid_x + [
            [ wrapcrement(x) for x in row ]
            for row in big_grid_y
        ]

    return solve_grid(big_grid_y)

DAY = "15"
lines = get_resource(f'day_{DAY}/input.txt').read_text().splitlines()


if __name__ == "__main":
    print(f"Answer 1 : {answer_1(lines)}")
    print(f"Answer 2 : {answer_2(lines)}")




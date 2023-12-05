from __future__ import annotations

from itertools import chain, permutations, pairwise

from typing import Sequence, List

class Route:

    start: str
    dest: str
    distance: int

    def __init__(self, line: str):
        start, _, dest, _, distance = line.split()
        self.start = start
        self.dest = dest
        self.distance = int(distance)

    def __repr__(self):
        return f'{self.start} -> {self.dest}'


def distances(lines: Sequence[str]):
    all_routes = [Route(line) for line in lines]

    routes = {
        route.start + route.dest: route for route in all_routes
    }

    places = set(chain.from_iterable(
        (route.start, route.dest) for route in all_routes
    ))

    journeys = permutations(places)

    def journey_route(stops):

        def get_route(a, b):
            key = a + b
            if not key in routes:
                key = b + a
            return routes[key]

        return [
            get_route(a, b) for a, b in pairwise(stops)
        ]

    trips = [journey_route(journey) for journey in journeys]

    def trip_distance(trip: List[Route]):
        return sum(leg.distance for leg in trip)

    distances = [
        trip_distance(trip) for trip in trips
    ]

    return distances

def answer_1(lines: Sequence[str]):
    return min(distances(lines))


def answer_2(lines: Sequence[str]):
    return max(distances(lines))

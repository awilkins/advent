from __future__ import annotations

from typing import Sequence, List

def get_reports(lines: Sequence[str]):
    return list(
        list(int(n) for n in line.split())
        for line in lines
    )

def is_safe(report: list[int]) -> bool:

    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    return all(
        0 < delta < 4 for delta in
        [abs(a - b) for a, b in zip(report, report[1:])]
    )

def dampen(report: list[int], pos: int) -> list[int]:
    return report[0:pos] + report[pos + 1:]

def is_safe_with_dampener(report: list[int]) -> bool:

    if (is_safe(report)):
        return True

    return any(is_safe(dampen(report, pos)) for pos in range(len(report)))


def answer_1(lines: Sequence[str]):
    reports = get_reports(lines)
    return sum(1 for report in reports if is_safe(report))


def answer_2(lines: Sequence[str]):
    reports = get_reports(lines)
    return sum(is_safe_with_dampener(report) for report in reports)

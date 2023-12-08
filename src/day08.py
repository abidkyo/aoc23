#!/usr/bin/env python3

"""
Count steps taken from start to end position.

Timing:
python3 = 48 ms
"""

from itertools import cycle
from aoc import lcm, read_input

# ------------------------------------------------------------------------------


def count_steps(instr, paths, start, end):
    instr = cycle(instr)
    element = start

    steps = 0
    while not element.endswith(end):
        rl = next(instr)
        element = paths.get(element)[rl == "R"]
        steps += 1

    return steps


def parse_maps(maps: str) -> dict:
    paths = {}

    for p in maps.splitlines():
        key, left = p.split(" = ")
        left, right = left.split(", ")
        paths[key] = (left[1:], right[:-1])

    return paths


def solve(day: int = 8, test: bool = False) -> tuple:
    """
    Part 1: count steps taken from start to end position.
    Part 2: count steps taken for every start positions to reach end position at the same time.
    """

    instr, maps = read_input(day, test).split("\n\n")
    paths = parse_maps(maps)

    start, end = "AAA", "ZZZ"
    part1 = count_steps(instr, paths, start, end)

    start, end = [k for k in paths.keys() if k.endswith("A")], "Z"
    part2 = lcm([count_steps(instr, paths, s, end) for s in start])

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (2, 2)

res = solve()
print(*res)
assert res == (14429, 10_921_547_990_923)

# ------------------------------------------------------------------------------

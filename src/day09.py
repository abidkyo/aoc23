#!/usr/bin/env python3

"""
Extrapolate a sequence with the interval values.

Timing:
python3 = 32 ms
"""

from aoc import integers, read_input

# ------------------------------------------------------------------------------


def extrapolate(seq: tuple) -> int:
    """
    Extrapolate sequence by generating new sequence from difference of each value
    until the latest sequence are zeros.
    The extrapolated values are the sum of last values in every sequence.
    """
    res = 0

    while set(seq) != {0}:
        diff = [n2 - n1 for n1, n2 in zip(seq[:-1], seq[1:])]

        res += seq[-1]
        seq = diff

    return res


def solve(day: int = 9, test: bool = False) -> tuple:
    """
    Part1: extrapolate forwards.
    Part2: extrapolate backwards.
    """
    txt = read_input(day, test).splitlines()

    part1 = sum(extrapolate(integers(t)) for t in txt)
    part2 = sum(extrapolate(integers(t)[::-1]) for t in txt)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (114, 2)

res = solve()
print(*res)
assert res == (1_757_008_019, 995)

# ------------------------------------------------------------------------------

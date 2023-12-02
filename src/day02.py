#!/usr/bin/env python3

"""
Parse digits in string.

Timing:
python3 = 25 ms
"""

from aoc import map_list, read_input
from math import prod
import re

# ------------------------------------------------------------------------------

COLORS_MAX = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_digits(data: str, part2: bool = False) -> int:
    """
    Part 1: Determine whether amount of colors less than allowed.
    Part 2: Determine minimum amount of colors needed.
    """

    maxs = [1]  # init with 1 for prod

    for color, max_amount in COLORS_MAX.items():
        amount = map_list(int, re.findall(r"(\d+) " + color, data))

        if part2:
            maxs.append(max(amount))
        elif max(amount) > max_amount:
            return 0

    return prod(maxs)


def solve(day=2, test=False):
    txt = read_input(day, test).splitlines()

    part1 = sum(i for i, data in enumerate(txt, 1) if parse_digits(data))
    part2 = sum(parse_digits(data, True) for data in txt)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (8, 2286)

res = solve()
print(*res)
assert res == (3059, 65371)

# ------------------------------------------------------------------------------

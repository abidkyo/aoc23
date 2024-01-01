#!/usr/bin/env python3

"""
Calculate hash and update list.

Timing:
python3: 26 ms
"""

from collections import defaultdict
from aoc import read_input

# ------------------------------------------------------------------------------


def calc_hash(string: str) -> int:
    hash = 0
    for ch in string:
        hash = ((hash + ord(ch)) * 17) % 256
    return hash


def solve(day: int = 15, test: bool = False) -> tuple[int, int]:
    txt = read_input(day, test).strip().split(",")

    part1 = 0
    part2 = 0

    BOX = defaultdict(list)

    for string in txt:
        part1 += calc_hash(string)

        if "=" in string:
            name, focal = string.split("=")
            hash = calc_hash(name)

            # update focal value or add item
            if name in (k for k, _ in BOX[hash]):
                BOX[hash] = [(k, int(focal) if k == name else v) for k, v in BOX[hash]]
            else:
                BOX[hash].append((name, int(focal)))

        elif "-" in string:
            name, _ = string.split("-")
            hash = calc_hash(name)

            # remove item
            BOX[hash] = [(k, v) for k, v in BOX[hash] if k != name]

    part2 = sum(
        (hash + 1) * slot * focal
        for hash, lens in BOX.items()
        for slot, (_, focal) in enumerate(lens, 1)
    )

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (1320, 145)

res = solve()
print(*res)
assert res == (509152, 244403)

# ------------------------------------------------------------------------------

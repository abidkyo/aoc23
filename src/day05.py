#!/usr/bin/env python3

"""
Number maps and ranges.

Timing:
python3 : 20 ms
"""

from aoc import integers, read_input

# ------------------------------------------------------------------------------


MAPS = []


def f(i: int, a: int, b: int) -> int:
    if i == len(MAPS):
        return a

    res = []
    for y, x1, r in MAPS[i]:
        x2 = x1 + r

        # no overlap
        if b <= x1 or a >= x2:
            continue

        # low range
        if a < x1:
            res.append(f(i, a, x1))

        # high range
        if b > x2:
            res.append(f(i, x2, b))

        # overlap range
        a, b = max(a, x1), min(b, x2)
        res.append(f(i + 1, a + y - x1, b + y - x1))
        break
    else:
        res.append(f(i + 1, a, b))

    return min(res)


def solve(day: int = 5, test: bool = False) -> tuple:
    global MAPS

    seeds, *blocks = read_input(day, test).split("\n\n")
    MAPS = [[integers(m) for m in b.splitlines()[1:]] for b in blocks]

    SEEDS = integers(seeds)
    part1 = min(f(0, seed, seed) for seed in SEEDS)

    SEEDS = [SEEDS[i : i + 2] for i in range(0, len(SEEDS), 2)]
    part2 = min(f(0, seed, seed + seed_len) for seed, seed_len in SEEDS)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (35, 46)

res = solve()
print(*res)
assert res == (331_445_006, 6_472_060)

# ------------------------------------------------------------------------------

#!/usr/bin/env python3

"""
Find the lower and upper bound.

Timing:
python3 = 1607 ms
pypy3 = 100 ms
"""

from math import prod
from aoc import integers, read_input

# ------------------------------------------------------------------------------


def count_win(t: tuple, d: tuple) -> int:
    lb = 0
    ub = 0

    # find first win from 1
    for t_button in range(1, t):
        d_travel = t_button * (t - t_button)

        if d_travel > d:
            lb = t_button
            break

    # find first win from t-1
    for t_button in reversed(range(lb, t)):
        d_travel = t_button * (t - t_button)

        if d_travel > d:
            ub = t_button
            break

    return ub - lb + 1


def solve(day: int = 6, test: bool = False) -> tuple:
    txt = read_input(day, test).splitlines()
    data = [t.split(":")[1] for t in txt]

    time, distance = [integers(d) for d in data]
    part1 = prod(count_win(time[i], distance[i]) for i in range(len(time)))

    time, distance = [integers(d.replace(" ", "")) for d in data]
    part2 = count_win(time[0], distance[0])

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (288, 71503)

res = solve()
print(*res)
assert res == (2065338, 34934171)

# ------------------------------------------------------------------------------

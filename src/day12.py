#!/usr/bin/env python3

"""
Count every possible arrangement of strings.

Timing:
python3: 261 ms
"""

from aoc import integers, read_input
from functools import lru_cache


# ------------------------------------------------------------------------------


def f(springs: str, count: tuple) -> int:
    N = len(springs)
    M = len(count)

    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        # return 1 if end of spring is reached and all count has been processed
        if i >= N:
            return int(j == M)

        res = 0

        # try to skip these characters
        if springs[i] in ".?":
            res += dp(i + 1, j)

        # try to put spring count in the next n spaces, IF
        # - there is still count to be processed, AND
        # - there is enough space, AND
        # - there is no '.' in the space, AND
        # - the end of spring is reached OR the next character after the space is not a "#"
        if springs[i] in "#?" and j < M:
            n = count[j]
            if i + n <= N and "." not in set(springs[i : i + n]) and (i + n == N or springs[i + n] != "#"):
                res += dp(i + n + 1, j + 1)

        return res

    return dp(0, 0)


def solve(day: int = 12, test: bool = False) -> tuple[int, int]:
    txt = read_input(day, test).splitlines()

    part1 = 0
    part2 = 0

    for t in txt:
        springs, count = t.split()
        count = integers(count)
        part1 += f(springs, count)

        # for part2, join springs 5 times with "?" and increase count blocks by 5
        springs = "?".join(springs for _ in range(5))
        count *= 5
        part2 += f(springs, count)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (21, 525152)

res = solve()
print(*res)
assert res == (7221, 7_139_671_893_722)

# ------------------------------------------------------------------------------

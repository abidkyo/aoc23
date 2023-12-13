#!/usr/bin/env python3

"""
Find point of relection.

Timing:
python3: 29 ms
"""

from aoc import list_transpose, read_input

# ------------------------------------------------------------------------------


def f(G: list[list[str]], R: int, C: int, p2: bool = False) -> int:
    def is_not_mirror(left, right):
        if 0 <= left < right < C:
            return sum(G[r][left] != G[r][right] for r in range(R))

        return 0

    res = 0
    for c in range(C - 1):
        not_mirror = 0
        for dc in range(C // 2):
            left = c - dc
            right = c + dc + 1
            not_mirror += is_not_mirror(left, right)

            # break here if found multiple errors
            if not_mirror > 1:
                break

        # part1: no reflection
        # part2: 1 error, if corrected, results in no reflection
        if not_mirror == (1 if p2 else 0):
            # break here because every grid contains only 1 reflection point
            res = c + 1
            break

    return res


def solve(day: int = 13, test: bool = False) -> tuple[int, int]:
    txt = read_input(day, test).split("\n\n")

    part1 = 0
    part2 = 0

    for grid in txt:
        G = [[c for c in row] for row in grid.splitlines()]
        GT = list_transpose(G)

        R = len(G)
        C = len(G[0])

        part1 += f(G, R, C)
        part1 += f(GT, C, R) * 100

        part2 += f(G, R, C, True)
        part2 += f(GT, C, R, True) * 100

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (405, 400)

res = solve()
print(*res)
assert res == (34100, 33106)

# ------------------------------------------------------------------------------

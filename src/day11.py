#!/usr/bin/env python3

"""
Point shifting and manhattan distance.

Timing:
python3: 71 ms
"""

from itertools import combinations
from aoc import list_transpose, manhattan_distance, read_input

# ------------------------------------------------------------------------------


def parse_galaxy(grid: list[str], factor: int) -> list[tuple]:
    """
    Return a list of galaxy positions after considering cosmic expansion.

    Note:
        A galaxy is denoted as '#' on the grid.

        Actual galaxy position differs from the grid position,
        due to cosmic expansion around empty rows and columns.
    """
    galaxies = []

    empty_rows = [set(row) == {"."} for row in grid]
    empty_cols = [set(row) == {"."} for row in list_transpose(grid)]

    ey = 0
    for y in range(len(grid)):
        if empty_rows[y]:
            ey += 1 * factor - 1

        ex = 0
        for x in range(len(grid[0])):
            if empty_cols[x]:
                ex += 1 * factor - 1

            if grid[y][x] == "#":
                galaxies.append((x + ex, y + ey))

    return galaxies


def solve(day: int = 11, test: bool = False) -> tuple[int, int]:
    """
    Part1: cosmic expansion with a factor of 2
    Part2: cosmic expansion with a factor of 1_000_000
    """
    txt = read_input(day, test).splitlines()

    galaxies = parse_galaxy(txt, 2)
    part1 = sum(manhattan_distance(a, b) for a, b in combinations(galaxies, 2))

    galaxies = parse_galaxy(txt, 1_000_000)
    part2 = sum(manhattan_distance(a, b) for a, b in combinations(galaxies, 2))

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (374, 82000210)

res = solve()
print(*res)
assert res == (9623138, 726820169514)

# ------------------------------------------------------------------------------

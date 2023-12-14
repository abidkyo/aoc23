#!/usr/bin/env pypy

"""
Tilt grid in every direction and cache usage.

Timing:
python3: 1832 ms
pypy: 1723 ms
"""

from aoc import DIR, read_input

# ------------------------------------------------------------------------------


def parse(txt: list[str]) -> tuple[set, set, int, int]:
    R = len(txt)
    C = len(txt[0])

    # add walls around the grid
    txt.insert(0, "#" * C)
    txt.append("#" * C)
    for r in range(R + 2):
        txt[r] = "#" + txt[r] + "#"

    R += 2
    C += 2

    rocks = set()
    walls = set()

    # store walls and rocks positions
    for y in range(R):
        for x in range(C):
            char = txt[y][x]

            if char == "#":
                walls.add((x, y))

            elif char == "O":
                rocks.add((x, y))

    return rocks, walls, R, C


def tilt_grid(
    rocks: set[tuple[int, int]],
    walls: set[tuple[int, int]],
    dx: int,
    dy: int,
) -> set[tuple[int, int]]:
    """
    Rocks are moved when grid is tilted.
    """
    new = set()

    def tilt(x: int, y: int) -> None:
        if (x, y) in walls or (x, y) in new:
            new.add((x - dx, y - dy))
            return None

        return tilt(x + dx, y + dy)

    # sort rocks by direction before tilting so that
    # rocks closer to direction-side are processed first
    [tilt(*rock) for rock in sorted(rocks, key=lambda x: (x[0] * -dx, x[1] * -dy))]

    assert len(new) == len(rocks)
    return new


def result(rocks: set[tuple[int, int]], R: int):
    return sum(R - 1 - y for _, y in rocks)


def solve(day: int = 14, test: bool = False) -> tuple[int, int]:
    """
    Part1: tilt to north and calculate load
    Part1: tilt in every direction for 1G times and calculate load
    """
    T = 1_000_000_000
    CACHE = {}

    txt = read_input(day, test).splitlines()
    ROCKS, WALLS, R, _ = parse(txt)

    part1 = 0
    part2 = 0

    t = 0
    while t < T:
        # tilt grid in every directions
        for j, d in enumerate("nwse"):
            d = DIR[d]

            ROCKS = tilt_grid(ROCKS, WALLS, *d)

            if t == 0 and j == 0:
                part1 = result(ROCKS, R)

        # cache function
        graph = tuple(ROCKS)
        if graph in CACHE:
            cycle = t - CACHE[graph]
            t += (T - t) // cycle * cycle
        CACHE[graph] = t

        t += 1

    part2 = result(ROCKS, R)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (136, 64)

res = solve()
print(*res)
assert res == (113424, 96003)

# ------------------------------------------------------------------------------

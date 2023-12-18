#!/usr/bin/env python3

"""
Find number of points covered by a polygon.

The answer is found by using Shoelace algorithm
and Pick's theorem.


Pick's theorem:
    A = I + B / 2 - 1
where:
    A: area of polygon
    I: no. of interior points
    B: no. of boundary points


Timing:
python3: 20 ms
"""

from aoc import DIR, read_input, shoelace

# ------------------------------------------------------------------------------


def solve(day: int = 18, test: bool = False) -> tuple[int, int]:
    txt = read_input(day, test).splitlines()

    x1, y1 = x2, y2 = 0, 0
    P1 = [(x1, y1)]
    P2 = [(x2, y2)]

    B1 = B2 = 0

    for t in txt:
        d, n, c = t.split(" ")
        dx, dy = DIR[d.lower()]
        n = int(n)

        x1 += n * dx
        y1 += n * dy

        B1 += n
        P1.append((x1, y1))

        d = int(c[-2])
        dx, dy = DIR[{0: "r", 1: "d", 2: "l", 3: "u"}[d]]
        n = int(c[2:-2], 16)

        x2 += n * dx
        y2 += n * dy

        B2 += n
        P2.append((x2, y2))

    # calc I using pick's theorem
    A = shoelace(P1)
    I1 = A - B1 // 2 + 1
    part1 = B1 + I1

    A = shoelace(P2)
    I2 = A - B2 // 2 + 1
    part2 = B2 + I2

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (62, 952408144115)

res = solve()
print(*res)
assert res == (41019, 96_116_995_735_219)

# ------------------------------------------------------------------------------

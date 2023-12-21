#!/usr/bin/env python3

"""
Shortest-path problem and parity.

Timing:
python3: 527 ms
"""

import numpy as np
from aoc import read_input

# ------------------------------------------------------------------------------


def solve(day: int = 21, test: bool = False) -> tuple:
    """
    Count reachable positions after:
    part1: 64 steps
    part2: 26501365 steps
    """
    txt = read_input(day, test).splitlines()

    P = complex

    R = len(txt)
    C = len(txt[0])

    walls = set()

    for r in range(R):
        for c in range(C):
            ch = txt[r][c]

            if ch == "S":
                start = P(r, c)

            elif ch == "#":
                walls.add(P(r, c))

    # ----------------------------------------------------------

    steps_p1 = 64
    steps_p2 = 26501365

    steps_needed = R // 2 + R * 2 + 1
    target = (steps_p2 - R // 2) // R

    X = np.array([0, 1, 2])
    Y = []

    parity = False

    pos = [start]
    seen = {}
    seen[start] = parity

    # ----------------------------------------------------------

    def wrap(p):
        return P(p.real % R, p.imag % C)

    def score():
        return sum(v == parity for v in seen.values())

    for s in range(steps_needed):
        if s % R == R // 2:
            Y.append(score())

        if s == steps_p1:
            part1 = score()

        new_pos = set()
        parity = not parity

        for p in pos:
            for d in (1, -1, 1j, -1j):
                npos = p + d

                if wrap(npos) not in walls and npos not in seen:
                    seen[npos] = parity
                    new_pos.add(npos)

        pos = new_pos

    coeff = np.rint(np.polyfit(X, Y, 2)).astype(int)[::-1]
    part2 = sum(target**X * coeff)

    return part1, part2


# ------------------------------------------------------------------------------

res = solve()
print(*res)
assert res == (3574, 600_090_522_932_119)

# ------------------------------------------------------------------------------

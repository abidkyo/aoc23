#!/usr/bin/env python3

"""
Find numbers and symbols in grid.

Timing:
python3: 25 ms
"""

from aoc import get_neighbour, read_input

# ------------------------------------------------------------------------------


def parse_data(txt: list) -> tuple:
    # append "." for easier parsing
    txt = [t + (".") for t in txt]

    G = [[c for c in row] for row in txt]
    R = len(G)
    C = len(G[0])

    N = {}
    S = []

    num = 0
    idx = 1

    for r in range(R):
        for c in range(C):
            ch = G[r][c]

            if ch.isdigit():
                num = num * 10 + int(ch)
                G[r][c] = idx
                continue

            if num != 0:
                N[idx] = num
                num = 0
                idx += 1

            if ch != ".":
                S.append((r, c))

    return G, N, S


def find_parts(G, S) -> tuple:
    R = len(G)
    C = len(G[0])

    PARTS = []
    GEARS = []

    for sr, sc in S:
        parts = set()

        for nc, nr in get_neighbour(sc, sr, amount=8):
            if not 0 <= nr < R and not 0 <= nc < C:
                continue

            n = G[nr][nc]
            if isinstance(n, int):
                parts.add(n)

        if G[sr][sc] == "*" and len(parts) == 2:
            GEARS.append(tuple(parts))

        PARTS.extend(parts)

    return PARTS, GEARS


def solve(day: int = 3, test: bool = False) -> tuple:
    """
    Part 1: sum of all part numbers
    Part 2: sum of all gear ratios
    """
    txt = read_input(day, test).splitlines()

    G, N, S = parse_data(txt)
    PARTS, GEARS = find_parts(G, S)

    part1 = sum(N[p] for p in PARTS)
    part2 = sum(N[g[0]] * N[g[1]] for g in GEARS)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (4361, 467835)

res = solve()
print(*res)
assert res == (532331, 82_301_120)

# ------------------------------------------------------------------------------

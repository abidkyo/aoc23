#!/usr/bin/env pypy

"""
Move along valid path and count the steps.

Timing:
python3: 2192 ms
pypy: 990 ms
"""

from aoc import DIR, read_input

# ------------------------------------------------------------------------------


def move(r: int, c: int, d: str) -> tuple[int, int, str]:
    dc, dr = DIR[d]
    return r + dr, c + dc, d


def bfs(grid: list[str], r: int, c: int, d: str) -> int:
    R, C = len(grid), len(grid[0])

    queue = [(r, c, d)]
    seen = set()
    points = set()

    while queue:
        r, c, d = queue.pop(0)
        if not (0 <= r < R and 0 <= c < C):
            continue

        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))

        points.add((r, c))

        ch = grid[r][c]
        if ch == "/":
            queue.append(move(r, c, {"u": "r", "r": "u", "d": "l", "l": "d"}[d]))

        elif ch == "\\":
            queue.append(move(r, c, {"u": "l", "r": "d", "d": "r", "l": "u"}[d]))

        elif ch == "|" and d in "rl":
            queue.extend([move(r, c, d) for d in "ud"])

        elif ch == "-" and d in "ud":
            queue.extend([move(r, c, d) for d in "rl"])

        else:
            queue.append(move(r, c, d))

    return len(points)


def solve(day: int = 16, test: bool = False) -> tuple[int, int]:
    G = read_input(day, test).splitlines()
    R, C = len(G), len(G[0])

    part1 = bfs(G, 0, 0, "r")

    part2 = 0
    for r in range(R):
        part2 = max(part2, bfs(G, r, 0, "r"))
        part2 = max(part2, bfs(G, r, C - 1, "l"))
    for c in range(C):
        part2 = max(part2, bfs(G, 0, c, "d"))
        part2 = max(part2, bfs(G, R - 1, c, "u"))

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (46, 51)

res = solve()
print(*res)
assert res == (6994, 7488)

# ------------------------------------------------------------------------------

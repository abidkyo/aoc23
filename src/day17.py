#!/usr/bin/env pypy

"""
Path finding with minimal cost using Dijsktra.

Timing:
python3: 4959 ms
pypy: 3552 ms
"""

from heapq import heappop, heappush
from aoc import DIR, read_input

# ------------------------------------------------------------------------------


DIR = [DIR[d] for d in "nwse"]


def dijkstra(G: list[list[int]], p2: bool) -> int:
    R, C = len(G), len(G[0])

    Q = [(0, 0, 0, -1, -1)]  # use -1 to indicate start
    D = {}

    while Q:
        cost, r, c, dir, cnt = heappop(Q)

        if (r, c) == (R - 1, C - 1):
            return cost

        if (r, c, dir, cnt) in D:
            continue
        D[(r, c, dir, cnt)] = cost

        # TODO: this can be faster
        # https://www.reddit.com/r/adventofcode/comments/18k9ne5/comment/kdqp7jx/
        for n_dir, (dc, dr) in enumerate(DIR):
            rr = r + dr
            cc = c + dc
            n_cnt = 1 if n_dir != dir else cnt + 1

            # not inbound or reversed
            if not (0 <= rr < R and 0 <= cc < C) or (n_dir + 2) % 4 == dir:
                continue

            # max steps == 3
            valid_p1 = n_cnt <= 3

            # max steps == 10, min steps == 4
            valid_p2 = n_cnt <= 10 and (n_dir == dir or cnt >= 4 or cnt == -1)
            valid = valid_p2 if p2 else valid_p1

            if not valid or (rr, cc, n_dir, n_cnt) in D:
                continue

            n_cost = cost + G[rr][cc]
            heappush(Q, (n_cost, rr, cc, n_dir, n_cnt))


def solve(day: int = 17, test: bool = False) -> tuple[int, int]:
    txt = read_input(day, test).splitlines()

    G = [[int(c) for c in row] for row in txt]

    part1 = dijkstra(G, False)
    part2 = dijkstra(G, True)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (102, 94)

res = solve()
print(*res)
assert res == (1246, 1389)

# ------------------------------------------------------------------------------

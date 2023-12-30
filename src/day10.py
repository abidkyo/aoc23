#!/usr/bin/env python3

"""
Paths and Points.

Note: It is necessary to enlarge grid to make 'flood' algorithm works.

Timing:
python3: 512 ms
pypy: 514 ms
"""

from aoc import get_neighbour, read_input, tuple_sum

# ------------------------------------------------------------------------------

FACTOR = 3

PIPE_MAPS = {
    "S": ((-1, 0), (1, 0), (0, -1), (0, 1)),
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "7": ((0, 1), (-1, 0)),
    "F": ((0, 1), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
}


def parse_input(data: list) -> tuple:
    points = set()
    pipes = dict()
    start = tuple()

    height = len(data)
    width = len(data[0])

    def translate(x: int, y: int) -> tuple:
        return x * FACTOR + 1, y * FACTOR + 1

    for y in range(height):
        for x in range(width):
            p = translate(x, y)
            points.add(p)

            char = data[y][x]

            if char == ".":
                continue
            if char == "S":
                start = p

            pipes[p] = PIPE_MAPS[char]

            for dx, dy in PIPE_MAPS[char]:
                nx, ny = tuple_sum(p, (dx, dy))
                pipes[nx, ny] = PIPE_MAPS["|"] if dx == 0 else PIPE_MAPS["-"]

    return points, pipes, start, height * FACTOR, width * FACTOR


def find_path(pipes: dict, start: tuple) -> set:
    """Find connected path of pipes using BFS."""

    queue = [start]
    visited = set()

    for p in queue:
        for d in pipes[p]:
            p_next = tuple_sum(p, d)

            if p_next in visited or p_next not in pipes:
                continue

            visited.add(p_next)
            queue.append(p_next)

    assert start in visited
    return visited


def get_outer_points(points: set, height: int, width: int) -> set:
    """
    Use BFS to 'flood' the grid.
    """
    p_outer = [(-1, 0), (0, -1)]
    visited = set()

    def valid_neighbour(p: tuple):
        return filter(
            lambda p: 0 <= p[0] < width and 0 <= p[1] < height,
            get_neighbour(*p),
        )

    for p in p_outer:
        for pn in valid_neighbour(p):
            if pn in points or pn in visited:
                continue

            visited.add(pn)
            p_outer.append(pn)

    return visited


def solve(day: int = 10, test: bool = False) -> tuple:
    """
    Part 1: steps taken along path to get to furthest point.
    Part 2: number of points enclosed in loop (pipe points in paths).
    """
    data = read_input(day, test).splitlines()
    points, pipes, start, height, width = parse_input(data)

    p_pipes = find_path(pipes, start)
    part1 = len(p_pipes) // 2 // FACTOR

    p_outer = get_outer_points(p_pipes, height, width)
    p_outside = p_outer | p_pipes

    part2 = len(points - p_outside)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (80, 10)

res = solve()
print(*res)
assert res == (7093, 407)

# ------------------------------------------------------------------------------

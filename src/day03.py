#!/usr/bin/env python3

"""

"""

from aoc import get_neighbour, print2d, read_input

# ------------------------------------------------------------------------------


# def solve(day=3, test=False):
#     txt = read_input(day, test).splitlines()

#     part1 = 0
#     part2 = 0

#     return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (4361, 0)

# res = solve()
# print(*res)
# assert res == (532331, 0)

# ------------------------------------------------------------------------------


def parse_grid(data: str):
    grid = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            char = data[y][x]

            grid[x, y] = char

    return grid


def valid(grid, x, y):
    get_neighbour(x, y, 8)
    return False


txt = read_input(3, True).splitlines()
txt = read_input(3, False).splitlines()
# grid = parse_grid(txt)
grid = txt

skip = False
numbers = [0]

coords = set()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        char = grid[y][x]

        if char != "." and not char.isdigit():
            # save numbers coord
            for nx, ny in get_neighbour(x, y, 8):
                if (grid[ny][nx]).isdigit():
                    coords.add((ny, nx))


coords = sorted(coords)

for ny, nx in coords:
    i = 0
    num = grid[ny][nx]

    # left
    for i in range(1, 3):
        val = grid[ny][nx - i]
        if val.isdigit():
            num = val + num
        else:
            break

    # right
    for i in range(1, 3):
        val = grid[ny][nx + i]
        if val.isdigit():
            num = num + val
        else:
            break

    if numbers[-1] != num:
        numbers.append(num)

print(sum(int(n) for n in numbers))

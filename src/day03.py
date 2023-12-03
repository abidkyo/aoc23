#!/usr/bin/env python3

"""

"""

from aoc import get_neighbour, print2d, printn, read_input

# ------------------------------------------------------------------------------


def parse_input(txt: list):
    num = 0
    nums_yx = {}

    for y in range(len(txt)):
        for x in range(len(txt[0])):
            c = txt[y][x]

            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if num:
                    x2 = x
                    nums_yx[(y, x)] = c

        #         if char != "." and not char.isdigit():
        #             # save numbers coord
        #             for nx, ny in get_neighbour(x, y, 8):
        #                 if (grid[ny][nx]).isdigit():
        #                     coords.add((ny, nx))

        nums_yx[((y, x1), (y, x2))] = char
    return nums_yx


def solve(day=3, test=False):
    txt = read_input(day, test).splitlines()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            char = grid[y][x]

            if char != "." and not char.isdigit():
                # save numbers coord
                for nx, ny in get_neighbour(x, y, 8):
                    if (grid[ny][nx]).isdigit():
                        coords.add((ny, nx))

    coords = sorted(coords)
    part1 = 0
    part2 = 0

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (4361, 467835)

# res = solve()
# print(*res)
# assert res == (532331, 82301120)

# ------------------------------------------------------------------------------


def valid(grid, x, y):
    get_neighbour(x, y, 8)
    return False


txt = read_input(3, True).splitlines()
# txt = read_input(3, False).splitlines()
# coords = set()

# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         char = grid[y][x]

#         if char != "." and not char.isdigit():
#             # save numbers coord
#             for nx, ny in get_neighbour(x, y, 8):
#                 if (grid[ny][nx]).isdigit():
#                     coords.add((ny, nx))


# coords = sorted(coords)

# numbers = [0]
# for ny, nx in coords:
#     i = 0
#     num = grid[ny][nx]

#     # left
#     for i in range(1, 3):
#         val = grid[ny][nx - i]
#         if val.isdigit():
#             num = val + num
#         else:
#             break

#     # right
#     for i in range(1, 3):
#         val = grid[ny][nx + i]
#         if val.isdigit():
#             num = num + val
#         else:
#             break

#     if numbers[-1] != num:
#         numbers.append(num)

# print(sum(int(n) for n in numbers))


# # p2 -----------------

# stars_coord = set()
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         char = grid[y][x]

#         stars = []
#         if char != "*":
#             # save numbers coord
#             for nx, ny in get_neighbour(x, y, 8):
#                 if (grid[ny][nx]).isdigit():
#                     stars.append((ny, nx))


res = 0
L = txt

NUMS = {}
IDX = 0
OCTDIR = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

for y, l in enumerate(L):
    W = len(l)
    i = 0
    num = 0

    def fix():
        global res, IDX
        IDX += 1
        j = i - 1
        added = False
        while j >= 0:
            if not l[j].isdigit():
                break
            NUMS[(j, y)] = (num, IDX)
            if not added:
                for dx, dy in OCTDIR:
                    x, ny = j + dx, y + dy
                    if 0 <= x < W and 0 <= ny < len(L):
                        c = L[ny][x]
                        if not c.isdigit() and c != ".":
                            res += num
                            added = True
            j -= 1

    while i < W:
        if l[i].isdigit():
            num = num * 10 + int(l[i])
        else:
            if num:
                fix()
            num = 0
        i += 1
    if num:
        fix()

print(res)
res = 0
print(type(NUMS))
printn(sorted(NUMS.items(), key=lambda x: x[1]))

for y, l in enumerate(L):
    for x, c in enumerate(l):
        if c == "*":
            nums = set()
            for dx, dy in OCTDIR:
                nx, ny = x + dx, y + dy
                v = NUMS.get((nx, ny))
                if v is not None:
                    nums.add(v)

            if len(nums) == 2:
                a, _ = nums.pop()
                b, _ = nums.pop()
                res += a * b

print(res)

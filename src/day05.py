#!/usr/bin/env python3

"""

"""

from aoc import INFINITY, integers, list_copy, list_flatten, printn, read_input

# ------------------------------------------------------------------------------


BEST = 0
maps = []


def tile(L, S: int) -> list:
    assert len(L) % S == 0
    return [L[i : i + S] for i in range(0, len(L), S)]


def f(i: int, l: int, r: int):
    global BEST
    if r <= l:
        return
    if i >= len(maps):
        BEST = min(BEST, l)
        return

    for sd, ss, llen in maps[i]:
        shift = sd - ss
        sr = ss + llen
        if r <= ss or sr <= l:
            continue

        if l < ss:
            assert r >= ss
            f(i, l, ss)
        if r > sr:
            assert l <= sr
            f(i, sr, r)

        l, r = max(l, ss), min(r, sr)
        f(i + 1, l + shift, r + shift)
        break
    else:
        f(i + 1, l, r)


def solve_p1(data: tuple) -> int:
    seeds = integers(seeds)


def solve_p2(data: tuple) -> int:
    seeds = integers(seeds)
    seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]


def solve(day=5, test=False):
    seeds, *map_blocks = read_input(day, test).split("\n\n")

    # parse seeds; 2nd line for p2
    seeds = integers(seeds)
    seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

    global maps
    maps = [[integers(map) for map in block.splitlines()[1:]] for block in map_blocks]

    global BEST
    BEST = 1 << 60

    for seed, seedlen in seeds:
        print(seed, seedlen)
        f(0, seed, seed + seedlen)

    print(BEST)

    part1 = 0
    part2 = 0

    return part1, part2


# ------------------------------------------------------------------------------

res = solve(test=True)
# assert res == (35, 46)

res = solve()
# print(*res)
# assert res == (331445006, 6472060)

exit()

# ------------------------------------------------------------------------------

# txt = read_input(5, True).split("\n\n")
# txt = read_input(5, False).split("\n\n")

# KEYS = ["se", "so", "fe", "wa", "li", "te", "hu", "lo"]

# data = {}

# for idx, t in enumerate(txt[1:]):
#     t = t.splitlines()

#     ranges = []
#     for i in range(1, len(t)):
#         ranges.append(integers(t[i]))

#     data[KEYS[idx + 1]] = ranges

# # printn(data.items())

# RESULT = INFINITY

# seeds = integers(txt[0])

# tmp = integers(txt[0])
# for i in range(0, len(tmp), 2):
#     print(i)
#     RES = 0
#     for s in range(tmp[i], tmp[i] + tmp[i + 1]):
#         new = s
#         for k in KEYS[1:]:
#             res = new
#             ranges = data[k]
#             for r in ranges:
#                 if r[1] <= res < (r[1] + r[2]):
#                     new = r[0] + res - r[1]

#             # print(res, k, new)
#         if new < RES:
#             RES = new
#             print("hi")
#             break
#         elif RES == 0:
#             RES = new
#         # print(s, new)

#     assert new == RES
#     print(s, RES)
#     if RES < RESULT:
#         RESULT = RES


# print("RES = ", RESULT)

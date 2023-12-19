#!/usr/bin/env python3

"""
Evaluate numbers according to rules.

Timing:
python3: 32 ms
"""

from math import prod
from aoc import read_input

# ------------------------------------------------------------------------------


def parse(workflows: str, parts_block: str) -> tuple[dict, list]:
    rules = {}
    for wf in workflows.splitlines():
        # chr(123) == '{'; the char breaks the autoindent :)
        name, rs = wf.split(chr(123))
        rs = rs[:-1].split(",")
        rules[name] = [r.split(":") for r in rs]

    parts = []
    for ps in parts_block.splitlines():
        ps = ps[1:-1].split(",")

        d = {}
        for p in ps:
            k, v = p.split("=")
            d[k] = int(v)

        parts.append(d)

    return rules, parts


def modify_part(cond: str, p: dict, np: dict) -> None:
    # dict is mutable; it is modified in-place

    key = cond[0]
    op = cond[1]
    lim = int(cond[2:])

    lo, hi = p[key]

    match op:
        case ">":
            p[key] = (lo, min(hi, lim))
            np[key] = (max(lo, lim + 1), hi)
        case "<":
            p[key] = (max(lo, lim), hi)
            np[key] = (lo, min(hi, lim - 1))


def process(workflows: dict, part: dict, p2: bool = False) -> int:
    def accepted(name: str, p: dict) -> int:
        if name == "A":
            if p2:
                return prod(b - a + 1 for a, b in p.values())
            else:
                return sum(p.values())

        elif name == "R":
            return 0

        rules = workflows[name]

        res = 0
        for r in rules:
            if len(r) == 1:
                res += accepted(r[0], p)
                break

            cond, dest = r

            if p2:
                np = dict(p)
                modify_part(cond, p, np)
                res += accepted(dest, np)
                continue

            if eval(cond, {}, p):
                res = accepted(dest, p)
                break

        return res

    start = "in"
    return accepted(start, part)


def solve(day: int = 19, test: bool = False) -> tuple[int, int]:
    """
    Part1: sum of part values if part is accepted.
    Part2: combination of part values, where part is accepted
    """
    workflows, parts_block = read_input(day, test).split("\n\n")
    workflows, parts = parse(workflows, parts_block)

    part1 = sum(process(workflows, part) for part in parts)

    part = {k: (1, 4000) for k in "xmas"}
    part2 = process(workflows, part, True)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (19114, 167_409_079_868_000)

res = solve()
print(*res)
assert res == (487623, 113_550_238_315_130)

# ------------------------------------------------------------------------------

#!/usr/bin/env python3

"""
Winning cards and numbers.

Timing:
python3 = 25 ms
"""

from aoc import integers, read_input

# ------------------------------------------------------------------------------


def solve(day=4, test=False):
    """
    Based on winning numbers:
        Part 1: calculate winning points.
        Part 2: calculate accumulated count of cards.
    """

    data = read_input(day, test).splitlines()

    card_count = [1] * len(data)

    part1 = 0
    part2 = 0

    for idx, line in enumerate(data):
        win_nums, nums = line.split(":")[1].split("|")
        win_nums = integers(win_nums)
        nums = integers(nums)

        wins = sum(1 for n in nums if n in win_nums)

        if wins > 0:
            # points double for every win => power of 2
            part1 += 2 ** (wins - 1)

        # Note: This would not execute for last card
        for i in range(wins):
            # N wins increase the next N cards by the card count
            card_count[idx + i + 1] += card_count[idx]

    part2 = sum(card_count)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (13, 30)

res = solve()
print(*res)
assert res == (21919, 9881048)

# ------------------------------------------------------------------------------

#!/usr/bin/env python3

"""
Find digits in string.

Timing:
python3 = 50 ms
"""

from aoc import en_digit, read_input

# ------------------------------------------------------------------------------


def find_add_digits(string: list, part2: bool = False) -> int:
    """Find digits in string and add the first and last digits."""

    digits = []
    for index, char in enumerate(string):
        if char.isdigit():
            digits.append(int(char))
        elif part2:
            if (val := en_digit(string[index:])) > 0:
                digits.append(val)

    return digits[0] * 10 + digits[-1]


def solve(day=1, test=False):
    txt = read_input(day, test).splitlines()

    data = txt[0:4] if test else txt
    part1 = sum(find_add_digits(string) for string in data)

    data = txt[4:] if test else txt
    part2 = sum(find_add_digits(string, True) for string in data)

    return part1, part2


# ------------------------------------------------------------------------------

# res = solve(test=True)
# assert res == (142, 281)

res = solve()
print(*res)
assert res == (55130, 54985)

# ------------------------------------------------------------------------------

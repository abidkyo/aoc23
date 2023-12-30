#!/usr/bin/env python3

"""
Count cards and rank players.

Timing:
python3 = 26 ms
"""

from aoc import map_list, map_tuple, read_input

# ------------------------------------------------------------------------------


def cards_rank(cards: str, p2: bool = False) -> tuple:
    RANKS = "J23456789TQKA" if p2 else "23456789TJQKA"
    return map_tuple(RANKS.find, cards)


def hand_rank(hand: str, p2: bool = False) -> tuple:
    counts = {card: hand.count(card) for card in hand}

    # add something before pop, so that counts has at least an item.
    counts["0"] = 0
    j_count = counts.pop("J", 0) if p2 else 0

    # get 2-best values (enough to rank player)
    rank = sorted(counts.values(), reverse=True)[:2]
    rank[0] += j_count

    return tuple(rank)


def solve(day: int = 7, test: bool = False) -> tuple:
    """
    Part 1: calculate winnings based on hand rank, bids and cards rank.
    Part 2: same as part 1, but "J" is replaced with the most count card.
    """
    txt = read_input(day, test).splitlines()
    players = map_list(str.split, txt)

    res = []
    for p2 in [False, True]:
        ranks = [(hand, bid, hand_rank(hand, p2)) for hand, bid in players]
        ranks = sorted(ranks, key=lambda x: (x[2], cards_rank(x[0], p2)))

        res.append(sum(rank * int(bid) for rank, (_, bid, _) in enumerate(ranks, 1)))

    return tuple(res)


# ------------------------------------------------------------------------------

# res = solve(test=True)
# print(*res)
# assert res == (6440, 5905)

res = solve()
print(*res)
assert res == (248_569_531, 250_382_098)

# ------------------------------------------------------------------------------

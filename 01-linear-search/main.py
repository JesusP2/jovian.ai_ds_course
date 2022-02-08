from typing import List


def locate_cards(cards: List[int], query: int) -> int:
    for i, x in enumerate(cards):
        if x == query:
            return i
    return -1

from typing import List


def get_rotations(cards: List[int]) -> int:
    if len(cards) == 0:
        return -1

    n = len(cards)
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        next = (mid + 1) % n
        prev = (mid - 1) % n
        if cards[mid] <= cards[prev] and cards[mid] <= cards[next]:
            return get_first(cards, mid)
        elif cards[mid] <= cards[hi]:
            hi = mid - 1
        elif cards[mid] >= cards[lo]:
            lo = mid + 1

    return 0


def get_first(cards: List[int], index: int) -> int:
    if index > 0 and cards[index - 1] == cards[index]:
        return get_first(cards, index - 1)
    return index


# linear search
def get_rotations_2(cards: List[int]) -> int:
    for i, x in enumerate(cards):
        next = (i + 1) % len(cards)
        if cards[i] > cards[next]:
            return next
        if x == cards[-1]:
            return 0
    return -1


if __name__ == '__main__':
    # inp = [5, 0, 1, 2, 4, 5]
    inp = [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    out = get_rotations(inp)
    print(out)

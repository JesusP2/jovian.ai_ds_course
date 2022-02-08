from typing import List
import time


# STEPS
# Select the middle as current_index
# If it matches the query, return the current_index
# Check if this value is bigger than the query
# If it's bigger then search on the first half
# Else, search on the second half
# If no more elements remain, return -1
## Generic Binary Search

# Here is the general strategy behind binary search, which is applicable to a variety of problems:
#
# 1. Come up with a condition to determine whether the answer lies before, after or at a given position
# 1. Retrieve the midpoint and the middle element of the list.
# 2. If it is the answer, return the middle position as the answer.
# 3. If answer lies before it, repeat the search with the first half of the list
# 4. If the answer lies after it, repeat the search with the second half of the list.
#
# Here is the generic algorithm for binary search, implemented in Python:


def locate_cards(cards: List[int], query: int, asc: bool = True) -> int:
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if cards[mid] == query:
            return get_first(cards, mid)
        elif query < cards[mid]:
            if asc:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if asc:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def get_first(cards: List[int], index: int) -> int:
    if index > 0 and cards[index - 1] == cards[index]:
        return get_first(cards, index - 1)
    return index


def get_last(cards: List[int], index: int) -> int:
    if index < (len(cards) - 1) and cards[index + 1] == cards[index]:
        return get_last(cards, index + 1)
    return index


if __name__ == "__main__":
    # O(n)
    start = time.time()
    inp = list(range(10000000))
    inp[500] = 499
    l_bound = locate_cards(inp, 499)
    r_bound = len(inp) - locate_cards(inp[::-1], 499, False)
    elapsed = time.time() - start
    print(elapsed, " : ", l_bound, r_bound, inp[l_bound:r_bound])

    # O(logN)
    start = time.time()
    l_bound = locate_cards(inp, 499)
    last = get_last(inp, l_bound)
    elapsed = time.time() - start
    print(elapsed, " : ", l_bound, last, inp[l_bound: last + 1])

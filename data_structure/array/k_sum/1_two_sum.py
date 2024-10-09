#!/usr/bin/env python3

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    >>> two_sum([3,2,4], 6)
    [1, 2]
    >>> two_sum([3,3], 6)
    [0, 1]
    """
    indices = []
    pair = {}

    for i, n in enumerate(nums):
        if n in pair:
            k = pair[n]
            indices = [k, i]
            break

        m = target - n
        pair[m] = i

    return indices

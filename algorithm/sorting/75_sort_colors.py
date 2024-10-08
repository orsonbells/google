#!/usr/bin/env python3

def sort_colors(nums: list[int]) -> list[int]:
    """
    >>> sort_colors([2,0,2,1,1,0])
    [0, 0, 1, 1, 2, 2]
    >>> sort_colors([2,0,1])
    [0, 1, 2]
    """
    k = 0
    l = 0
    r = len(nums) - 1

    while k <= r:
        if 0 == nums[k]:
            nums[l], nums[k] = nums[k], nums[l]
            l += 1
            k += 1
        elif 1 == nums[k]:
            k += 1
        else:
            nums[r], nums[k] = nums[k], nums[r]
            r -= 1

    return nums


def sort_colors_count(nums: list[int]) -> list[int]:
    """
    >>> sort_colors_count([2,0,2,1,1,0])
    [0, 0, 1, 1, 2, 2]
    >>> sort_colors_count([2,0,1])
    [0, 1, 2]
    """
    counts = {0: 0, 1: 0, 2: 0}
    for n in nums:
        counts[n] += 1
    i = 0
    for k, v in counts.items():
        for j in range(v):
            nums[i] = k
            i += 1

    return nums

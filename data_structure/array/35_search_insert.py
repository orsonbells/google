#!/usr/bin/env python3

def search_insert(nums: list[int], target: int) -> int:
    """
    >>> search_insert([1,3,5,6], 5)
    2
    >>> search_insert([1,3,5,6], 2)
    1
    >>> search_insert([1,3,5,6], 7)
    4
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        if target > nums[m]:
            l = m + 1
        if target < nums[m]:
            r = m - 1

    return l

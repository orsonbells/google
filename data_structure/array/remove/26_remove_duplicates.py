#!/usr/bin/env python3

def remove_duplicates(nums: list[int]) -> int:
    """
    >>> remove_duplicates([1,1,2])
    2
    >>> remove_duplicates([0,0,1,1,1,2,2,3,3,4])
    5
    """
    k = 0
    seen_nums = set()
    for n in nums:
        if n not in seen_nums:
            seen_nums.add(n)
            nums[k] = n
            k += 1
    return k

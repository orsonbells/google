#!/usr/bin/env python3

def remove_element(nums: list[int], val: int) -> int:
    """
    >>> remove_element([3,2,2,3], 2)
    2
    >>> remove_element([0,1,2,2,3,0,4,2], 2)
    5
    """
    k = 0
    for n in nums:
        if val != n:
            nums[k] = n
            k += 1
    return k

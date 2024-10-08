#!/usr/bin/env python3


def merge_sorted_array(nums_m: list[int], m: int, nums_n: list[int], n: int) -> list[
    int]:
    """
    >>> merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3)
    [1, 2, 2, 3, 5, 6]
    >>> merge_sorted_array([1], 1, [], 0)
    [1]
    >>> merge_sorted_array([0], 0, [1], 1)
    [1]
    """
    i = m - 1
    j = n - 1
    k = (m + n) - 1

    while i >= 0 and j >= 0:
        a = nums_m[i]
        b = nums_n[j]

        if a > b:
            nums_m[k] = a
            i -= 1
        else:
            nums_m[k] = b
            j -= 1

        k -= 1

    nums_m[:j + 1] = nums_n[:j + 1]

    return nums_m

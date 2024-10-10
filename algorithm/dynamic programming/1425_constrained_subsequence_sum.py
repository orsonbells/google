#!/usr/bin/env python3

def constrained_subsequence_sum(nums: list[int], k: int) -> int:
    """
    >>> constrained_subsequence_sum([10,2,-10,5,20], 2)
    37
    >>> constrained_subsequence_sum([-1,-2,-3], 1)
    -1
    >>> constrained_subsequence_sum([10,-2,-10,-5,20], 2)
    23
    """
    max_sums = [0] * len(nums)

    for i in range(len(nums)):
        cur_sum = max(max_sums[max(0, i - k):i + 1])
        max_sums[i] = cur_sum + nums[i]

    return max(max_sums)

#!/usr/bin/env python3
from collections import deque


def constrained_subsequence_sum_deque(nums: list[int], k: int) -> int:
    """
    >>> constrained_subsequence_sum_deque([10,2,-10,5,20], 2)
    37
    >>> constrained_subsequence_sum_deque([-1,-2,-3], 1)
    -1
    >>> constrained_subsequence_sum_deque([10,-2,-10,-5,20], 2)
    23
    """
    max_sums = [0] * len(nums)
    max_deque = deque()

    for i in range(len(nums)):
        if max_deque and i > k + max_deque[0]:
            max_deque.popleft()

        cur_sum = max(0, max_sums[max_deque[0]]) if max_deque else 0
        max_sums[i] = nums[i] + cur_sum

        while max_deque and max_sums[i] >= max_sums[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(i)

    return max(max_sums)

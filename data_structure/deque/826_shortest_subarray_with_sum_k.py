#!/usr/bin/env python3
from collections import deque


def shortest_subarray_sum_k_deque(nums: list[int], k: int) -> int:
    """
    >>> shortest_subarray_sum_k_deque([1], 1)
    1
    >>> shortest_subarray_sum_k_deque([1,2], 4)
    -1
    >>> shortest_subarray_sum_k_deque([2,-1,2], 3)
    3
    >>> shortest_subarray_sum_k_deque([48,99,37,4,-31], 140)
    2
    """
    sums = [0]
    for num in nums:
        sums.append(num + sums[-1])

    min_deque = deque([0])
    min_length = float('inf')

    for i in range(1, len(nums) + 1):
        while min_deque and sums[i] >= k + sums[min_deque[0]]:
            j = min_deque[0]
            min_length = min(i - j, min_length)
            min_deque.popleft()

        while min_deque and sums[min_deque[-1]] >= sums[i]:
            min_deque.pop()

        min_deque.append(i)

    if float('inf') == min_length:
        return -1

    return min_length

#!/usr/bin/env python3
import heapq


def constrained_subsequence_sum_heap(nums: list[int], k: int) -> int:
    """
    >>> constrained_subsequence_sum_heap([10,2,-10,5,20], 2)
    37
    >>> constrained_subsequence_sum_heap([-1,-2,-3], 1)
    -1
    >>> constrained_subsequence_sum_heap([10,-2,-10,-5,20], 2)
    23
    """
    max_heap_k = [(-nums[0], 0)]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        while i > k + max_heap_k[0][1]:
            heapq.heappop(max_heap_k)

        max_sum_k = max(0, -max_heap_k[0][0])
        cur_sum = nums[i] + max_sum_k
        heapq.heappush(max_heap_k, (-cur_sum, i))

        max_sum = max(cur_sum, max_sum)

    return max_sum

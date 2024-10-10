#!/usr/bin/env python3
import heapq


def shortest_subarray_sum_k_heap(nums: list[int], k: int) -> int:
    """
    >>> shortest_subarray_sum_k_heap([1], 1)
    1
    >>> shortest_subarray_sum_k_heap([1,2], 4)
    -1
    >>> shortest_subarray_sum_k_heap([2,-1,2], 3)
    3
    >>> shortest_subarray_sum_k_heap([48,99,37,4,-31], 140)
    2
    """
    cur_sum = 0
    min_heap = [(cur_sum, -1)]
    min_length = float('inf')

    for i in range(len(nums)):
        cur_sum += nums[i]
        while min_heap and cur_sum >= k + min_heap[0][0]:
            j = min_heap[0][1]
            min_length = min(i - j, min_length)
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, (cur_sum, i))

    if float('inf') == min_length:
        return -1

    return min_length

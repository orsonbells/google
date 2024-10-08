#!/usr/bin/env python3

def three_sum_closest(nums: list[int], target: int) -> int:
    """
    >>> three_sum_closest([-1,2,1,-4], 1)
    2
    >>> three_sum_closest([0,0,0], 1)
    0
    """

    nums.sort()
    closest_sum = float('inf')
    n = len(nums)

    for i in range(n - 2):
        j = i + 1
        k = n - 1
        current_sum = nums[i] + nums[j] + nums[k]

        current_distance = target - current_sum
        closest_distance = target - closest_sum

        if abs(current_distance) < abs(closest_distance):
            closest_sum = current_sum

        if current_distance > 0:
            k -= 1
        if current_distance < 0:
            j += 1
        if current_distance == 0:
            break

    return closest_sum

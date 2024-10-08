#!/usr/bin/env python3

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    >>> three_sum([-1,0,1,2,-1,-4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([0,1,1])
    []
    >>> three_sum([0,0,0])
    [[0, 0, 0]]
    """

    three_sums = []
    nums.sort()
    n = len(nums)

    seen_v = set()
    for i in range(n - 2):
        if nums[i] in seen_v:
            continue
        seen_v.add(nums[i])

        j = i + 1
        k = n - 1

        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if current_sum < 0:
                j += 1
            if current_sum > 0:
                k -= 1
            if current_sum == 0:
                three_nums = [nums[i], nums[j], nums[k]]
                three_sums.append(three_nums)
                while j < k and nums[j+1] == nums[j]:
                    j += 1
                while k > j and nums[k-1] == nums[k]:
                    k -= 1
                j += 1
                k -= 1

    return three_sums

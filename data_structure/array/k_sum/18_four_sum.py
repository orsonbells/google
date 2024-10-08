#!/usr/bin/env python3

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    >>> four_sum([1,0,-1,0,-2,2], 0)
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    >>> four_sum([2,2,2,2,2], 8)
    [[2, 2, 2, 2]]
    """

    four_sums = []
    nums.sort()
    n = len(nums)
    seen_v = set()

    for i in range(n - 3):
        if nums[i] in seen_v:
            continue
        seen_v.add(nums[i])

        seen_w = set()
        for j in range(i + 1, n - 2):
            if nums[j] in seen_w:
                continue
            seen_w.add(nums[j])

            k = j + 1
            l = n - 1

            while k < l:
                current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if current_sum < target:
                    k += 1
                if current_sum > target:
                    l -= 1
                if current_sum == target:
                    four_nums = [nums[i], nums[j], nums[k], nums[l]]
                    four_sums.append(four_nums)
                    while k < l and nums[k + 1] == nums[k]:
                        k += 1
                    while l > k and nums[l - 1] == nums[l]:
                        l -= 1
                    k += 1
                    l -= 1

    return four_sums

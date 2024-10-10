#!/usr/bin/env python3

def min_k_bit_flips(nums: list[int], k: int) -> int:
    """
    >>> min_k_bit_flips([0,1,0], 1)
    2
    >>> min_k_bit_flips([1,1,0], 2)
    -1
    >>> min_k_bit_flips([0,0,0,1,0,1,1,0], 3)
    3
    """
    n = len(nums)
    num_flips = 0

    is_flipped = 0
    for i in range(n):
        if i >= k and nums[i - k] < 0:
            is_flipped ^= 1
            nums[i - k] += 2

        if 0 == (nums[i] ^ is_flipped):
            if i + k > n:
                return -1

            num_flips += 1
            is_flipped ^= 1
            nums[i] -= 2

    return num_flips

#!/usr/bin/env python3

def counting_bits(n: int) -> list[int]:
    """
    >>> counting_bits(2)
    [0, 1, 1]
    >>> counting_bits(5)
    [0, 1, 1, 2, 1, 2]
    >>> counting_bits(9)
    [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]
    """
    bits = [0] * (n + 1)

    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)

    return bits

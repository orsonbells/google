#!/usr/bin/env python3

def climbing_stairs(n: int) -> int:
    """
    >>> climbing_stairs(2)
    2
    >>> climbing_stairs(3)
    3
    """
    num_ways = [1] * (n + 1)

    for i in range(2, n + 1):
        num_ways[i] = num_ways[i - 1] + num_ways[i - 2]

    return num_ways[n]

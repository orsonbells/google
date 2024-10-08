#!/usr/bin/env python3

def pascals_triangle_ii(n: int) -> list[int]:
    """
    >>> pascals_triangle_ii(3)
    [1, 3, 3, 1]
    >>> pascals_triangle_ii(0)
    [1]
    >>> pascals_triangle_ii(1)
    [1, 1]
    """
    row = [1] * (n + 1)

    for k in range(1, n + 1):
        row[k] = row[k - 1] * (n - k + 1)
        row[k] //= k

    return row

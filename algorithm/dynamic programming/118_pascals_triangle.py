#!/usr/bin/env python3

def pascals_triangle(num_rows: int) -> list[list[int]]:
    """
    >>> pascals_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascals_triangle(1)
    [[1]]
    """
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            n = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row[j] = n
        triangle.append(row)

    return triangle

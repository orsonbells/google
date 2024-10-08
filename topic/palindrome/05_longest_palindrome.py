#!/usr/bin/env python3

def longest_palindrome(s: str) -> str:
    """
    >>> longest_palindrome('babad')
    'bab'
    >>> longest_palindrome('cbbd')
    'bb'
    """

    def palindrome(i: int, j: int) -> str:
        while (i >= 0) and (j < len(s)) and (s[i] == s[j]):
            i -= 1
            j += 1

        return s[i + 1: j]

    max_p = ''

    for k in range(len(s)):
        p_odd = palindrome(k, k)
        p_even = palindrome(k, k + 1)
        max_p = max(max_p, p_odd, p_even, key=len)

    return max_p

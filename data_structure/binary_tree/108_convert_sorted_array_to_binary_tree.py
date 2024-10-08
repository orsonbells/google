#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def convert_sorted_array_to_binary_tree(nums: list[int]) -> TreeNode | None:
    def array_to_binary_tree(l: int, r: int) -> TreeNode | None:
        if l > r:
            return None

        m = (l + r) // 2
        left = array_to_binary_tree(l, m - 1)
        right = array_to_binary_tree(m + 1, r)
        root = TreeNode(nums[m], left, right)

        return root

    binary_tree = array_to_binary_tree(0, len(nums) - 1)
    return binary_tree

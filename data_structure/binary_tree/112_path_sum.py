#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def path_sum(root: TreeNode | None, target: int) -> bool:
    def has_path_sum(node: TreeNode | None, target_sum: int) -> bool:
        if not node:
            return False

        target_sum -= node.val

        if not (node.left or node.right):
            return 0 == target_sum

        return has_path_sum(node.left, target_sum) or has_path_sum(node.right,
                                                                   target_sum)

    return has_path_sum(root, target)

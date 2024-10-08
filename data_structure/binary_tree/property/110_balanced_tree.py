#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def balanced_tree(root: TreeNode | None) -> bool:
    def is_balanced(node: TreeNode | None) -> int:
        if not node:
            return 0

        l = is_balanced(node.left)
        r = is_balanced(node.right)

        if (l == -1) or (r == -1) or (abs(l - r) > 1):
            return -1

        return 1 + max(l, r)

    return is_balanced(root) >= 0

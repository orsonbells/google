#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def min_depth(root: TreeNode | None) -> int:
    def depth(node: TreeNode | None) -> int:
        if not node:
            return 0

        if not node.left:
            return 1 + depth(node.right)
        if not node.right:
            return 1 + depth(node.left)

        return 1 + min(depth(node.left), depth(node.right))

    return depth(root)

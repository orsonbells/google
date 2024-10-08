#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def max_depth(root: TreeNode | None) -> int:
    def depth(node: TreeNode | None) -> int:
        if not node:
            return 0

        return 1 + max(depth(node.left), depth(node.right))

    num_nodes = depth(root)
    return num_nodes

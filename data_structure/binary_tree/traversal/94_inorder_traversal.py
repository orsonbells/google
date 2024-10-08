#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def inorder_traversal(root: TreeNode | None) -> list[int]:
    def inorder(node: TreeNode | None):
        if not node:
            return []

        return inorder(node.left) + [node.val] + inorder(node.right)

    return inorder(root)

#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def preorder_traversal(root: TreeNode | None) -> list[int]:
    def preorder(node: TreeNode | None):
        if not node:
            return []

        return [node.val] + preorder(node.left) + preorder(node.right)

    return preorder(root)

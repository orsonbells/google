#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def postorder_traversal(root: TreeNode | None) -> list[int]:
    def postorder(node: TreeNode | None):
        if not node:
            return []

        return postorder(node.left) + postorder(node.right) + [node.val]

    return postorder(root)

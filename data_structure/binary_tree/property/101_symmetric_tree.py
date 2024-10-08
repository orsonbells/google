#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def symmetric_tree(root: TreeNode | None) -> bool:
    def is_symmetric(p: TreeNode | None, q: TreeNode | None) -> bool:
        if not (p or q):
            return True
        if p and q:
            return (
                (p.val == q.val)
                and is_symmetric(p.right, q.left)
                and is_symmetric(p.left, q.right)
            )
        return False

    return is_symmetric(root.left, root.right)

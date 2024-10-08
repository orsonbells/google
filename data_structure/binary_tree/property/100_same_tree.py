#!/usr/bin/env python3


from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    def is_same(r: TreeNode | None, s: TreeNode | None) -> bool:
        if not (r or s):
            return True
        if r and s:
            return (
                (r.val == s.val)
                and is_same(r.left, s.left)
                and is_same(r.right, s.right)
            )
        return False

    return is_same(p, q)

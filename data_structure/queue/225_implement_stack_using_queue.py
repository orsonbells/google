#!/usr/bin/env python3

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(-1)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue

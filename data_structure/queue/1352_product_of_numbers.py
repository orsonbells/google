#!/usr/bin/env python3

class ProductOfNumbers:

    def __init__(self):
        self.prods = [1]

    def add(self, num: int) -> None:
        if num:
            self.prods.append(self.prods[-1] * num)
        else:
            self.prods = [1]

    def get_product(self, k: int) -> int:
        if len(self.prods) < (k + 1):
            return 0
        return self.prods[-1] // self.prods[-(k + 1)]

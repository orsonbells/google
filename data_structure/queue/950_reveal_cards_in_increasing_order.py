#!/usr/bin/env python3

def deck_reveal_increasing(deck: list[int]) -> list[int]:
    """
    >>> deck_reveal_increasing([17,13,11,2,3,5,7])
    [2, 13, 3, 11, 5, 17, 7]
    >>> deck_reveal_increasing([1,1000])
    [1, 1000]
    """
    n = len(deck)
    order_deck = list(range(n))
    order_in_which_cards_are_revealed = list(range(n))
    deck.sort()

    for i in range(n):
        first = order_in_which_cards_are_revealed.pop(0)
        order_deck[first] = deck[i]

        if order_in_which_cards_are_revealed:
            second = order_in_which_cards_are_revealed.pop(0)
            order_in_which_cards_are_revealed.append(second)
    
    return order_deck

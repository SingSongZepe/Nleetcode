

from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        # receive [0 ... n]
        def f(cards: List[int]) -> List[int]:
            if len(cards) <= 2:
                return cards

            if len(cards) % 2 == 0:
                return cards[0:len(cards):2] + f(cards[1:len(cards):2])
            else:
                return cards[0:len(cards):2] + f(cards[3:len(cards):2] + cards[1:2])

        res = [0] * len(deck)
        for o, v in zip(f([i for i in range(len(deck))]), sorted(deck)):
            res[o] = v

        return res




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
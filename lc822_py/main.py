

from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        total = set(fronts + backs)

        for front, back in zip(fronts, backs):
            if front == back:
                total.discard(front)

        return min(total, default=0)

class Solution1:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        return min(set(fronts + backs) - set([front for front, back in zip(fronts, backs) if front == back]), default=0)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
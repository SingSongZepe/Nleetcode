
from typing import List




class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0

        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)


class Solution1:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(1 for p in position if p % 2 == i) for i in (0, 1))


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
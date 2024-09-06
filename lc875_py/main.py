

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left



        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
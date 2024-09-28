
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if candy + extraCandies >= max(candies) else False for candy in candies]

class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [True if candy >= threshold else False for candy in candies]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
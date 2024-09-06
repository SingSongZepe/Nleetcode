

from typing import List
from functools import cache
from itertools import accumulate

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# nice solution using dynamic programming and caching
class Solution1:
    def stoneGame(self, a: List[int]) -> bool:
        @cache
        def f(i, j):
            if i <= j:
                return p[j] - (i and p[i - 1]) - min(f(i + 1, j), f(i, j - 1))

            return 0

        p = [*accumulate(a)]

        return f(0, len(a) - 1) > p[-1] / 2



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
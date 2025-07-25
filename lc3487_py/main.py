
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        d = set()
        res = 0
        max_neg = float('-inf')
        added = False

        for n in nums:
            if n in d:
                continue
            if n <= 0 and not added:
                if n > max_neg:
                    max_neg = n
                continue
            res += n
            added = True
            d.add(n)

        return res if added else max_neg


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
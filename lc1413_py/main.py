

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tot = nums[0]
        m = tot

        for n in nums[1:]:
            tot += n
            if m > tot:
                m = tot

        return 1 if m > 0 else -m + 1


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
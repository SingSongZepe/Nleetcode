

from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        n, m = len(flips), 0
        sum = 0
        cnt = 0

        for flip in flips:
            m = max(m, flip)
            sum += flip
            if sum == (m + 1) * m // 2:
                cnt += 1

        return cnt

class Solution1:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ml = 0
        cnt = 0
        for idx, flip in enumerate(flips, start=1):
            if flip > ml:
                ml = flip
            if idx == ml:
                cnt += 1

        return cnt

def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        m1, m2 = 0, 0

        for n in nums:
            if n > m2:
                m2, m1 = n, m2
            elif n > m1:
                m1 = n

        return (m1 - 1) * (m2 - 1)




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
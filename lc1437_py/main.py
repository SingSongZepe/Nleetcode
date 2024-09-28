

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        i = -k-1

        for j, n in enumerate(nums):
            if n == 1:
                if j - i <= k:
                    return False
                else:
                    i = j

        return True



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
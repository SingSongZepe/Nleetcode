

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        res = []
        for n, i in zip(nums, index):
            res.insert(i, n)

        return res







def main():
    print('Hello World')

if __name__ == '__main__':
    main()
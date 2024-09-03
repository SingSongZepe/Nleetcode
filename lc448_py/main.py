

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        appeared = [False] * len(nums)
        for num in nums:
            appeared[num-1] = True

        return [i+1 for i in range(len(nums)) if not appeared[i]]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
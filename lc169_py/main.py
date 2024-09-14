

from typing import List

class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        candidate = -1
        votes = 0

        for i in range(n):
            if votes == 0:
                candidate = arr[i]
                votes = 1
            else:
                if arr[i] == candidate:
                    votes += 1
                else:
                    votes -= 1
        count = 0

        for i in range(n):
            if arr[i] == candidate:
                count += 1

        if count > n // 2:
            return candidate
        else:
            return -1


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = None

        for num in nums:
            if count == 0:
                majority_element = num
            count += (1 if num == majority_element else -1)

        return majority_element


# boyer-moore majority vote algorithm
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
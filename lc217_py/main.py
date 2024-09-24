

from typing import List


# O(nlogn) time O(1) space solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False


# O(n) time O(n) space solution
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

# O(n**2) time O(1) space solution
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


# one-liner, O(n) time O(n) space solution
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))










def main():
    print('Hello World')

if __name__ == '__main__':
    main()
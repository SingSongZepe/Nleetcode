

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        arr = [0] * n
        arr[0] = 1

        res = []
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                 arr[i] = 1

        for j in range(k-1, n):
            for i in range(j-k+2, j+1):
                if arr[i] == 0:
                    res.append(-1)
                    break
            else:
                res.append(nums[j])

        return res


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        n = len(nums)
        res = []

        for j in range(k-1, n):
            for i in range(j-k+2, j+1):
                if nums[i] != nums[i-1] + 1:
                    res.append(-1)
                    break
            else:
                res.append(nums[j])

        return res


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        n = len(nums)
        res = []
        start = 0

        for i in range(1, n):
            if nums[i] != nums[i-1] + 1:
                start = i
            if i - start + 1 >= k:
                res.append(nums[i])
            elif i >= k - 1:
                res.append(-1)

        return res








def main():
    print('Hello World')

if __name__ == '__main__':
    main()
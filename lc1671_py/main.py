

from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        def get_removal(nums: List[int]) -> List[int]:
            stk = [float('inf')]
            removal = [0] * len(nums)

            for i, n in enumerate(nums):
                for j in range(len(stk) - 1, -1, -1):
                    if stk[j] < n:
                        removal[i] = i - j - 1
                        if j == len(stk) - 1:
                            stk.append(n)
                        else:
                            stk[j + 1] = n
                        break
                else:
                    stk[0] = n
                    removal[i] = 1001

            return removal

        removal_front = get_removal(nums)
        removal_rear = get_removal(nums[::-1])

        mi = 1001
        n = len(nums)
        for i in range(1, n-1):
            mi = min(removal_front[i] + removal_rear[n-i-1], mi)

        return mi

from bisect import bisect_left

class Solution1:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        n = len(nums)

        def get_lis(arr):
            res = [0] * n
            stack = []
            for i in range(n):
                if stack and stack[-1] >= arr[i]:
                    j = bisect_left(stack, arr[i])
                    stack[j] = arr[i]
                    res[i] = j+1
                else:
                    stack.append(arr[i])
                    res[i] = len(stack)
            return res

        removal_front = get_lis(nums)
        removal_rear = get_lis(nums[::-1])[::-1]

        mi = 1001
        for i in range(n):
            if removal_front[i] > 1 and removal_rear[i] > 1:
                mi = min(mi, n - (removal_front[i] + removal_rear[i]-1))

        return mi

# my new solution using lis
class Solution2:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        n = len(nums)

        def get_lis(nums: List[int]):
            stk = []
            lis = [0] * n

            for i in range(n):
                if stk and stk[-1] >= nums[i]:
                    idx = bisect_left(stk, nums[i])
                    stk[idx] = nums[i]
                    lis[i] = idx + 1
                else:
                    stk.append(nums[i])
                    lis[i] = len(stk)
            return lis

        l, r = get_lis(nums), get_lis(nums[::-1])

        mi = 997
        for i, j in zip(range(n), range(n-1,-1,-1)):
            if l[i] > 1 and r[j] > 1:
                mi = min(mi, n-(l[i]+r[j])+1)

        return mi

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
import bisect
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        nn = len(arr)

        l, r = 0, nn - 1
        while l < r:
            if arr[l+1] >= arr[l]:
                l += 1
            elif arr[r-1] <= arr[r]:
                r -= 1
            else:
                break

        if (r == l - 1 or r == l) and arr[l] <= arr[r]:
            return 0

        mx = 0
        arr2 = arr[r:]
        m, n = l+1, nn - r
        for i in range(m):
            j = bisect.bisect_left(arr2, arr[i])
            tot = i + 1 + n - j
            if tot > mx:
                mx = tot

        return nn - max(m, n, mx)

# maybe a better solution
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ret = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            # find next valid number after arr[left]
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            # save length of removed subarray
            ret = min(ret, right - left - 1)
            left += 1
        return ret
        # time: O(n)
        # space: O(1)


class Solution1:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # sentinel
        arr.append(float("inf"))
        arr.insert(0, 0)

        left = 0
        right = len(arr) - 1
        shortest = float("inf")

        while left < len(arr) - 2 and arr[left] <= arr[left + 1]:
            left += 1

        while left >= 0:
            while right - 1 > left and arr[right - 1] >= arr[left] and arr[right] >= arr[right - 1]:
                right -= 1
            shortest = min(shortest, right - left - 1)
            left -= 1

        return shortest


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
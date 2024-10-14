

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        lst = [1] * n
        fre = [1] * n

        for i in range(1, n):
            j = i - 1
            while j >= 0 and arr[i] <= arr[j]:
                j -= 1
            fre[i] = i - j

        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and arr[i] < arr[j]:
                j += 1
            lst[i] = j - i

        return sum(arr[i] * lst[i] * fre[i] for i in range(n))







# this is solution for the problem
# that is to find the sum of all subarray minimums in an array
class FakeSolution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        s = 0
        for i in range(len(arr)):
            s += arr[i] * ((i+1)*(len(arr)-i))

        return s

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
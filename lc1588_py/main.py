

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                n += sum(arr[i:j+1])
        return n


class Solution1:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum([((i+1) * (len(arr)-i) + 1) // 2 * arr[i] for i in range(len(arr))])







def main():
    print('Hello World')

if __name__ == '__main__':
    main()
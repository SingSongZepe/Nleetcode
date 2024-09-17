

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1

        return n - l


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
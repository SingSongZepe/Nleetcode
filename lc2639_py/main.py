

from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        def count_len(v: int) -> int:
            if v == 0:
                return 1

            l = 0 if v > 0 else 1
            v = abs(v)
            while v:
                l += 1
                v //= 10

            return l

        m, n = len(grid), len(grid[0])
        res = [0] * n

        for r in range(m):
            for c in range(n):
                res[c] = max(res[c], count_len(grid[r][c]))

        return res



def count_len(v: int) -> int:
    if v == 0:
        return 1

    l = 0 if v > 0 else 1
    v = abs(v)
    while v:
        l += 1
        v //= 10

    return l

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
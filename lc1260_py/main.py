

from typing import List


# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m, n, ans = len(grid), len(grid[0]), []
#         for i in range(m):
#             ans.append([])
#             for j in range(n):
#                 d = (i * n + j - k) % (m * n)
#                 ans[-1].append(grid[d//n][d%n])
#         return ans

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n, res = len(grid), len(grid[0]), []

        k = k % (m*n)

        if k == 0:
            return grid

        for i in range(m):
            res.append([])
            for j in range(n):
                l = (i*n+j-k) % (m*n)
                res[-1].append(grid[l//n][l%n])

        return res

        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
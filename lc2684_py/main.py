

from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        stk = [(i, 0) for i in range(m)]
        mm = 0

        while stk:
            nstk = set()
            for _ in range(len(stk)):
                r, c = stk.pop()

                if c == n-1:
                    return c
                if c > mm:
                    mm = c

                # top
                if r > 0:
                    if grid[r-1][c+1] > grid[r][c]:
                        nstk.add((r-1, c+1))
                # bottom
                if r < m-1:
                    if grid[r+1][c+1] > grid[r][c]:
                        nstk.add((r+1, c+1))
                if grid[r][c+1] > grid[r][c]:
                    nstk.add((r, c+1))

            stk.extend(list(nstk))

        return mm

class Solution1:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        stk = [i for i in range(m-1, -1, -1)]
        stk = [i for i in range(m-1, -1, -1)]
        curr_c = 0

        while stk:
            nstk = set()
            for _ in range(len(stk)):
                r = stk.pop()

                # top
                if r > 0:
                    if grid[r-1][curr_c+1] > grid[r][curr_c]:
                        nstk.add(r-1)
                # bottom
                if r < m-1:
                    if grid[r+1][curr_c+1] > grid[r][curr_c]:
                        nstk.add(r+1)
                if grid[r][curr_c+1] > grid[r][curr_c]:
                    nstk.add(r)

            if len(nstk) == 0:
                return curr_c

            stk.extend(list(nstk))

            curr_c += 1
            if curr_c == n-1:
                return curr_c

        return curr_c

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
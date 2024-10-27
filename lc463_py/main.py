

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = 0
                if grid[i][j] == 1:
                    curr = 4
                    if  j > 0 and grid[i][j-1] == 1:
                        curr -= 1
                    if  j < len(grid[0])-1 and grid[i][j+1] == 1:
                        curr -= 1
                    if  i > 0 and grid[i-1][j] == 1:
                        curr -= 1
                    if  i < len(grid)-1 and grid[i+1][j] == 1:
                        curr -= 1
                tot += curr
        return tot


# better solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 4
                    if i > 0 and grid[i - 1][j] == 1:  # top (to connect with down:current position)
                        result -= 2
                    if j > 0 and grid[i][j - 1] == 1:  # left (to connect with right: current position)
                        result -= 2

        return result


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
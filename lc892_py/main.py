

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        # m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                if height:
                    area += 2 + height * 4 # top and bottom and four sides
                    if i:
                        area -= min(height, grid[i - 1][j]) * 2  # cover sides
                    if j:
                        area -= min(height, grid[i][j - 1]) * 2  # cover sides
        return area




class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface_area = 0

        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                if height:
                    surface_area += 2 + height * 4
                    if i:
                        surface_area -= min(height, grid[i - 1][j]) * 2
                    if j:
                        surface_area -= min(height, grid[i][j - 1]) * 2

        return surface_area

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
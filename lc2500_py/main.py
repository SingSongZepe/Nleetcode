

from typing import List
import heapq

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapq.heapify(row)

        tot = 0
        for _ in range(len(grid[0])):
            m = 0
            for row in grid:
                v = heapq.heappop(row)
                if v > m:
                    m = v
            tot += m

        return tot





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
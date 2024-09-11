

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        dirs = [(-1, 1), (1, -1)]
        r, c, d = 0, 0, 0
        m, n = len(mat), len(mat[0])

        for _ in range(m * n):
            print((r, c))
            res.append(mat[r][c])
            dr, dc = dirs[d]

            if d == 0: # up
                if c + dc >= n:
                    r += 1
                    d = 1
                elif r + dr < 0:
                    c += 1
                    d = 1
                else:
                    r += dr
                    c += dc
            else: # down
                if r + dr >= m:
                    c += 1
                    d = 0
                elif c + dc < 0:
                    r += 1
                    d = 0
                else:
                    r += dr
                    c += dc

        return res





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
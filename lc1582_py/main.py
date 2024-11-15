

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        st_c = set()
        def unique(r: int, c: int) -> bool:

            for i in range(m):
                if mat[i][c] == 1 and i != r:
                    return False

            if sum(mat[r]) == 1:
                st_c.add(c)
                return True
            return False

        cnt = 0
        for i in range(m):
            for j in range(n):
                if j in st_c:
                    continue
                if mat[i][j] == 1 and unique(i, j):
                    cnt += 1
                    break

        return cnt

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        for i in mat:
            if sum(i) == 1:
                ind = i.index(1)
                if sum([mat[r][ind] for r in range(len(mat))]) == 1:
                    cnt += 1
        return cnt











        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
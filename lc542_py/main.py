

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq = deque()
        MAX_DISTANCE = m + n

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dq.append((r, c))
                else:
                    mat[r][c] = MAX_DISTANCE

        while dq:
            r, c = dq.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[r][c] + 1:
                    dq.append((nr, nc))
                    mat[nr][nc] = mat[r][c] + 1

        return mat


from math import inf

# best solution
class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])

        for r in range(n):
            for c in range(m):
                if mat[r][c]!=0:
                    top = mat[r-1][c] if r>0 else inf
                    left = mat[r][c-1] if c>0 else inf

                    mat[r][c] = min(top,left)+1

        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if mat[r][c]!=0:
                    bot = mat[r+1][c] if r<n-1 else inf
                    right =  mat[r][c+1] if c<m-1 else inf

                    mat[r][c] = min(mat[r][c], bot+1, right+1)

        return mat


# time out
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        # 初始化结果矩阵
        dp = [[inf] * m for _ in range(n)]

        # 首先将所有水池位置的距离设为0
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    dp[r][c] = 0

        # 四个方向的偏移量
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上

        # 进行多次迭代，直到没有更新
        for _ in range(n * m):  # 最多进行 n*m 次迭代
            updated = False
            for r in range(n):
                for c in range(m):
                    if mat[r][c] == 1:  # 只更新陆地
                        current_distance = dp[r][c]
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m:
                                current_distance = min(current_distance, dp[nr][nc] + 1)
                        if current_distance < dp[r][c]:
                            dp[r][c] = current_distance
                            updated = True
            if not updated:  # 如果没有更新，提前结束
                break

        return dp

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
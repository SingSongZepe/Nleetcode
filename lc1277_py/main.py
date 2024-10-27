
from typing import List

class Solution:
    def countSquares(self, dp: List[List[int]]) -> int:
        row = len(dp)
        col = len(dp[0])

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        ans = 0
        for rows in dp:
            ans += sum(rows)
        return ans

# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#
#
#
#
#         pass

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
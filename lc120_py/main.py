

from typing import List


# DP solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = [0] * len(triangle)

        for i in range(len(triangle)):
            if i > 0:
                dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):

                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]

        return min(dp)










        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()



# longest common subsequence LCS solution
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = dp[0]
            for j in range(1, n + 1):
                tmp = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = prev + ord(s2[j-1])
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = tmp

        return sum(ord(c) for c in s1 + s2) - 2 * dp[n]

class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = dp[0]
            for j in range(1, n + 1):
                tmp = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = prev + ord(s2[j-1])
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = tmp

        return sum(ord(c) for c in s1 + s2) - 2 * dp[n]


# longest common subsequence LCS solution
class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # Create a 1D DP array to store the LCS lengths
        dp = [0] * (n + 1)

        # Calculate the LCS lengths
        for i in range(1, m + 1):
            prev = dp[0]  # store the value of the previous row's first element
            for j in range(1, n + 1):
                temp = dp[j]  # store the current value of dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev + ord(s1[i - 1])
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp  # update prev to store the value of dp[j]

        # Calculate the sum of ASCII values of characters not part of LCS
        sum_ascii = 0
        for c in s1:
            sum_ascii += ord(c)
        for c in s2:
            sum_ascii += ord(c)

        return sum_ascii - 2 * dp[n]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
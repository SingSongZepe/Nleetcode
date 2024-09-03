

from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        for num in range(1, int(sqrt(n)) + 1):
            if num * num > n:
                continue

            square = num * num
            for targetIdx in range(1, n + 1):
                if targetIdx % square == 0:
                    dp[targetIdx] = targetIdx // square
                else:
                    dp[targetIdx] = min((targetIdx // square) + dp[targetIdx%square], dp[targetIdx])

        return dp[-1]


class Solution1:
    def numSquares(self, n: int) -> int:
        if sqrt(n) == int(sqrt(n)):
            return 1

        perfect_squares: list[int] = [
            num ** 2
            for num in range(1, int(sqrt(n)) + 1)
        ]

        for total_summands in range(2, n + 1):
            least_summands_found = False

            def supportive_function(summands: int, sum: int) -> None:
                nonlocal least_summands_found

                if least_summands_found:
                    return
                elif summands == total_summands:
                    if sum == n:
                        least_summands_found = True
                    return

                for summand in perfect_squares:
                    supportive_function(summands + 1, sum + summand)

            supportive_function(0, 0)
            if least_summands_found:
                return total_summands


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        stk = []
        profit = 0
        n = len(prices)
        for i in range(n):
            while stk and stk[-1] > prices[i]:
                stk.pop()
            stk.append(prices[i])
            if len(stk) >= 2 and i < n-1 and prices[i+1] < prices[i]:
                profit += stk[-1] - stk[0]
                stk = []

        if len(stk) >= 2:
            profit += stk[-1] - stk[0]

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = prices[0]
        high = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < high:
                profit += high - low
                low = prices[i]
                high = prices[i]
            else:
                high = prices[i]

        return profit + high - low


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
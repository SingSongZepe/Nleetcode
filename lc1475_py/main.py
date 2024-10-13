

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = [prices[-1]]

        for i in range(len(prices) - 2, -1, -1):
            while stack and prices[i] < stack[-1]:
                stack.pop()

            tmp = prices[i]
            if stack:
                prices[i] -= stack[-1]

            stack.append(tmp)

        return prices


class Solution1:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
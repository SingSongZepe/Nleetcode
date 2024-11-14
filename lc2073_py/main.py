

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        tot = 0
        curr = tickets[k]
        for i in tickets[:k+1]:
            tot += min(i, curr)

        for i in tickets[k+1:]:
            tot += min(i, curr-1)

        return tot






def main():
    print('Hello World')

if __name__ == '__main__':
    main()
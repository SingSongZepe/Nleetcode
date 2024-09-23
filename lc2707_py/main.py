

from typing import List

from collections import defaultdict

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        st = set(dictionary)
        shortest = min(len(w) for w in st)
        last_dict = defaultdict(list)
        for w in st:
            last_dict[w[-1]].append(w)

        dp = [0] * (len(s) + 1)
        for i in range(shortest):
            dp[i] = i

        for i in range(shortest, len(s) + 1):

            res = dp[i - 1] + 1

            for w in last_dict[s[i - 1]]:
                if w == s[i - len(w):i]:
                    res = min(res, dp[i - len(w)])

            dp[i] = res
        return dp[-1]



class Solution1:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1

            for length in range(1, n - i + 1):
                if s[i:i + length] in wordSet:
                    dp[i] = min(dp[i], dp[i + length])

        return dp[0]

import collections

class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        short = float('inf')
        book = collections.defaultdict(list)

        for w in dictionary:
            short = min(short, len(w))
            book[w[-1]].append(w)

        dp = [i for i in range(short)]

        for i in range(short, len(s) + 1):

            res = dp[i - 1] + 1

            for w in book[s[i - 1]]:
                if len(w) > i:
                    continue

                if w == s[i - len(w):i]:
                    res = min(res, dp[i - len(w)])
            dp.append(res)

        return dp[-1]

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
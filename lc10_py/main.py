
import re

import re


# DFS and DP solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}
        m, n = len(s), len(p)

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= m and j >= n:
                return True
            if j >= n:
                return False

            match_current = p[j] == '.' or s[j] == p[j]
            if j + 1 < n and p[j + 1] == '*':
                cache[(i, j)] = dfs(i, j+2) or (match_current and dfs(i+1, j))
                return cache[(i, j)]
            if match_current:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)





class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(p)
        return pattern.fullmatch(s) is not None




class Solution2:
    def isMatch(self, s: str, p: str) -> bool:

        # TOP-Down Memoization

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)


class RegexAutomaton:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def is_match(self, text: str) -> bool:
        return self._dp(0, 0, text, self.pattern)

    def _dp(self, i: int, j: int, text: str, pattern: str) -> bool:
        if j == len(pattern):
            return i == len(text)

        first_match = (i < len(text)) and (pattern[j] == text[i] or pattern[j] == '.')

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            return (self._dp(i, j + 2, text, pattern) or  # 不使用'*'
                    (first_match and self._dp(i + 1, j, text, pattern)))  # 使用'*'
        else:
            return first_match and self._dp(i + 1, j + 1, text, pattern)

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        return RegexAutomaton(p).is_match(s)




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
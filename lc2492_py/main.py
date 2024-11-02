

from typing import List
from collections import defaultdict


# BFS solution
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        d = defaultdict(list)
        for f, t, w in roads:
            d[f].append((t, w))
            d[t].append((f, w))

        dq = [1]
        visited = set(dq)
        mi = 10000

        while dq:
            for _ in dq:
                f = dq.pop()
                for t, w in d[f]:
                    if w < mi:
                        mi = w
                    if t in visited:
                        continue
                    visited.add(t)
                    dq.append(t)

        return mi


# DFS solution
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        d = [[] for _ in range(n+1)]
        for f, t, w in roads:
            d[f].append((t, w))
            d[t].append((f, w))

        visited = set()
        mi = 10000

        def dfs(curr: int):
            visited.add(curr)
            nonlocal mi
            for t, w in d[curr]:
                if w < mi:
                    mi = w
                if t in visited:
                    continue
                dfs(t)

        dfs(1)
        return mi


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List, Set, Tuple
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        es = [[] for _ in range(n)]
        for f, t in edges:
            es[f].append(t)
            es[t].append(f)

        visited = set()

        def dfs(f: int):
            visited.add(f)
            for t in es[f]:
                if t not in visited:
                    dfs(t)

        dfs(source)
        return destination in visited


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
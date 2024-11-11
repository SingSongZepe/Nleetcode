

from typing import List
from collections import deque

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        n = len(coins)
        d = [[] for _ in range(n)]
        for f, t in edges:
            d[f].append(t)
            d[t].append(f)

        degrees = list(map(len, d))

        dq = deque()
        for i in range(n):
            if degrees[i] == 1:
                if coins[i]:
                   dq.append((i, True))
                else:
                    dq.appendleft((i, True))

        deleted = 0
        while dq:
            curr, is_leaf = dq.popleft()
            deleted += 1

            for next in d[curr]:
                degrees[next] -= 1

                if is_leaf and degrees[next] == 1:
                    if coins[curr]:
                        dq.append((next, False))
                    elif coins[next]:
                        dq.append((next, True))
                    else:
                        dq.appendleft((next, True))

        return 2 * max(0, n - 1 - deleted)




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
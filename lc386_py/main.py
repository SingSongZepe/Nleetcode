

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        res = []

        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            dfs(curr * 10)
            if curr % 10 != 9:
                dfs(curr + 1)

        dfs(1)
        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
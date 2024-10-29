

from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        d = {i: [] for i in range(n)}
        for f, t in edges:
            d[f].append(t)
            d[t].append(f)
        st = set()
        gcnt = 0

        for i in range(n):
            if i in st:
                continue

            # bfs
            stk = [i]
            curr_st = {i}
            while stk:
                for _ in stk:
                    nd = stk.pop()
                    st.add(nd)
                    for nnd in d[nd]:
                        if nnd not in st:
                            stk.append(nnd)
                            curr_st.add(nnd)
                            st.add(nnd)

            complete = True
            for nd in curr_st:
                if len(d[nd]) != len(curr_st) - 1:
                    complete = False
                    break

            if complete:
                gcnt += 1

        return gcnt

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        d = {i: [] for i in range(n)}
        for f, t in edges:
            d[f].append(t)
            d[t].append(f)
        st = set()
        gcnt = 0

        # mark
        def dfs(nd: int):
            curr_st.add(nd)
            st.add(nd)
            for nnd in d[nd]:
                if nnd not in st:
                    dfs(nnd)


        for i in range(n):
            if i in st:
                continue

            # dfs
            curr_st = set()
            dfs(i)

            complete = True
            for nd in curr_st:
                if len(d[nd]) != len(curr_st) - 1:
                    complete = False
                    break

            if complete:
                gcnt += 1

        return gcnt











        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
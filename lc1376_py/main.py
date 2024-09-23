

from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        mtime = 0
        visited = set()

        def dfs(m: int, t: int) -> int:
            visited.add(m)
            t += informTime[m]
            if m == -1 or m == headID:
                return t
            t = max(t, dfs(manager[m], t))
            return t

        for m in manager:
            if m in visited:
                continue
            mtime = max(mtime, dfs(m, 0))

        return mtime


class Solution1:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        leader_map = defaultdict(list)

        for i, m in enumerate(manager):
            leader_map[m].append(i)

        def dfs(leader: int) -> int:
            if leader not in leader_map:
                return 0
            mtime = 0
            for sleader in leader_map[leader]:
                mtime = max(mtime, informTime[leader] + dfs(sleader))
            return mtime


        return dfs(headID)



class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        master_maps = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                master_maps[m].append(i)

        def get_time_inform(leader):
            if leader not in master_maps:
                return 0
            max_time = 0
            for sub_leader in master_maps[leader]:
                max_time = max(max_time, informTime[leader] + get_time_inform(sub_leader))
            return max_time

        return get_time_inform(headID)



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
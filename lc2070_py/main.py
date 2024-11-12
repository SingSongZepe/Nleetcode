import bisect
from typing import List
from math import inf

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort()
        d = {}
        qs = []
        for q in queries:
            idx = bisect.bisect_left(items, [q, inf])
            mb = 0
            for i in range(idx-1, -1, -1):
                if i in d:
                    mb = max(mb, d[i])
                    break
                if items[i][1] > mb:
                    mb = items[i][1]
            d[idx-1] = mb
            qs.append(mb)

        return qs

# maybe a better solution
class Solution(object):
    def maximumBeauty(self, items, queries):

        maxI = float('inf')
        res = [[0, 0, maxI]]

        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            lastBracket = res[-1]
            if beauty > lastBracket[1]:
                res[-1][2] = price
                res.append([price, beauty, maxI])

        ans = []

        for x in queries:
            for i in range(len(res) - 1, -1, -1):
                if res[i][0] <= x:
                    ans.append(res[i][1])
                    break

        return ans

class Solution(object):
    def maximumBeauty(self, items, queries):

        res = [[0, 0]]

        items.sort()

        for price, beauty in items:
            last = res[-1]
            if beauty > last[1]:
                res.append([price, beauty])

        ans = []

        for x in queries:
            idx = bisect.bisect_left(res, [x, inf])
            ans.append(res[idx-1][1])

        return ans



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
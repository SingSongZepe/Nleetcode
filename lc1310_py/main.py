

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pxors = [arr[0]]
        for i in range(1, len(arr)):
            pxors.append(pxors[i-1] ^ arr[i])

        res = []
        for l, r in queries:
            if l == 0:
                res.append(pxors[r])
            else:
                res.append(pxors[r] ^ pxors[l-1])

        return res

class Solution1:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pxors = [0] * len(arr)
        for i in range(1, len(arr) + 1):
            pxors[i] = pxors[i-1] ^ arr[i-1]

        res = []
        for l, r in queries:
            res.append(pxors[r+1] ^ pxors[l])

        return res


class Solution2(object):
    def xorQueries(self, arr, queries):
        n = len(arr)

        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] ^ arr[i - 1]

        ans = []
        for l, r in queries:
            ans.append(pref[l] ^ pref[r + 1])
        return ans


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def balancedString(self, s: str) -> int:

        hash = {
            'Q': 0,
            'W': 1,
            'E': 2,
            'R': 3,
        }

        n = len(s) // 4

        cnt = [0] * 4
        for c in s:
            cnt[hash[c]] += 1

        if all([v == n for v in cnt[1:]]):
            return 0

        l = 0
        need = [v - n if v > n else 0 for v in cnt]
        curr = [0] * 4
        lst = sum(need)
        mi = float('inf')

        for r in range(len(s)):
            curr[hash[s[r]]] += 1

            if all([curr[i] >= need[i] for i in range(4) if need[i] != 0]):
                while l <= r:
                    c = hash[s[l]]
                    curr[c] -= 1

                    mi = min(mi, r-l+1)
                    l += 1
                    if mi == lst:
                        return lst

                    if curr[c] < need[c]:
                        break

        return mi


class Solution1:
    def balancedString(self, s: str) -> int:
        Max = len(s) // 4
        d = {
            'Q': 0,
            'W': 0,
            'E': 0,
            'R': 0,
        }

        l, r = 0, len(s) - 1

        # grow left to max
        while l < len(s):
            c = s[l]
            if d[c] == Max:
                # cant grow anymore
                l -= 1
                break
            d[c] += 1
            l += 1

        # no replacement needed
        if l == len(s):
            return 0

        res = r - l

        # slowly grow right and reduce left, track length of substring
        while r > l:
            c = s[r]
            if d[c] == Max:
                while l >= 0:
                    leftC = s[l]
                    d[leftC] -= 1
                    l -= 1
                    if leftC == c:
                        break
                else:
                    # no more such char in the left portion
                    # reached end state
                    break
            d[c] += 1
            res = min(res, r - l - 1)
            r -= 1

        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
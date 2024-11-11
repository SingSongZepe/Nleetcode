

from typing import List
from string import ascii_lowercase

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        d1 = {chars[i]: vals[i] for i in range(len(chars))}
        d2 = {c: i for i, c in enumerate(ascii_lowercase, start=1)}
        curr = 0
        mv = 0

        for c in s:
            v = d1[c] if c in d1 else d2[c]
            if v < 0:
                mv = max(curr, mv)
            curr = max(0, curr + v)

        return max(curr, mv)


class Solution1:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        d = {c: i for i, c in enumerate(ascii_lowercase, start=1)}
        for c, v in zip(chars, vals):
            d[c] = v
        curr = 0
        mv = 0

        for c in s:
            curr += d[c]
            if curr < 0:
                curr = 0
            mv = max(mv, curr)

        return mv


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        d = [i+1 for i in range(26)]
        for c, v in zip(chars, vals):
            d[ord(c)-97] = v
        curr = 0
        mv = 0

        for c in s:
            curr += d[ord(c)-97]
            if curr < 0:
                curr = 0
            mv = max(mv, curr)

        return mv


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
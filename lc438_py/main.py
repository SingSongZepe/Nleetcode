

from typing import List
from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []
        i = 0

        need = Counter(p)
        curr = defaultdict(int)
        start = -1
        while i < len(s):
            if s[i] not in need:
                curr = defaultdict(int)
                start = i
                i += 1
                continue

            curr[s[i]] += 1
            if i - len(p) > start:
                curr[s[i-len(p)]] -= 1

            if need == curr:
                res.append(i-len(p)+1)

            i += 1

        return res











        pass

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
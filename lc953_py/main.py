

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i

        def compare(w1, w2) -> bool:
            p = 0
            m, n = len(w1), len(w2)

            while p < m and p < n:
                if w1[p] == w2[p]:
                    p += 1
                    continue
                return d[w1[p]] <= d[w2[p]]

            if p == n == m:
                return True
            if p == n:
                return False
            return True

        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False

        return True



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
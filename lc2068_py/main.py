

from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        d1, d2 = Counter(word1), Counter(word2)
        st = set(word1 + word2)

        for i in st:
            if abs(d1[i]-d2[i]) > 3:
                return False

        return True

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        d = Counter(word1)

        for c in word2:
            d[c] -= 1

        if any(abs(i) > 3 for _, i in d.items()):
            return False

        return True



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
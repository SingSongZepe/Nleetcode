

from typing import List, Set, FrozenSet
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        res = [words[0]]
        prev_sorted = sorted(words[0])

        for i in range(1, len(words)):
            f = sorted(words[i])
            if prev_sorted == f:
                continue
            res.append(words[i])
            prev_sorted = f

        return res


















        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
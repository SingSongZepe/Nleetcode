

from typing import List
from collections import Counter


class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words)
        m = len(words[0])
        diff = []
        for i in range(n):
            cur = []
            for j in range(m - 1):
                cur.append(ord(words[i][j + 1]) - ord(words[i][j]))
            diff.append(tuple(cur))

        cnt = Counter(diff)
        for i in range(n):
            if cnt[diff[i]] == 1:
                return words[i]


class Solution1:
    def oddString(self, words: List[str]) -> str:

        word_int = []
        l = []
        unique_min = 0

        for word in words:
            for i in range(len(word)):
                if (i != len(word) - 1):
                    l.append(ord(word[i + 1]) - ord(word[i]))
            word_int.append(' '.join(str(x) for x in l))
            l = []

        word_int_count = Counter(word_int)

        for i in word_int_count:
            if (word_int_count[i] == 1):
                unique_min = i
                break

        for i in range(len(word_int)):
            if (word_int[i] == unique_min):
                return words[i]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

# another problem solution
# indicate how many characters in the word are present in the string
# select the longest one
class AnotherProblemSolution:  # mistaking the meaning of the problem
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def compare(s: str, w: str) -> int:
            if len(s) < len(w):
                return -1

            cnt = 0
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(w):
                if s[p1] == w[p2]:
                    cnt += 1
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1

            return cnt

        ml = 0
        mstack = []

        for w in dictionary:
            v = compare(s, w)
            if v == 0:
                continue
            elif v == ml:
                mstack.append(w)
            elif v > ml:
                ml = v
                mstack = [w]

        mstack.sort()
        return mstack[0] if mstack else ""


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def isSubsequence(s: str, w: str) -> bool:
            it = iter(s)
            return all(char in it for char in w)

        longest_word = ""

        for w in dictionary:
            if isSubsequence(s, w):
                if len(w) > len(longest_word) or (len(w) == len(longest_word) and w < longest_word):
                    longest_word = w

        return longest_word






        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
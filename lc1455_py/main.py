
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        p1, p2 = 0, 0
        m, n = len(sentence), len(searchWord)
        cnt = 1

        while p1 < m:
            if sentence[p1] == searchWord[p2]:
                p2 += 1
                if p2 == n:
                    return cnt
            else:
                while p1 < m and sentence[p1] != ' ':
                    p1 += 1
                cnt += 1
                p2 = 0
            p1 += 1

        return -1



class Solution1:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), start=1):
            if word.startswith(searchWord):
                return i
        return -1




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
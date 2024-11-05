
class Solution:
    def minChanges(self, s: str) -> int:

        n = len(s)
        cnt = 0
        for i, j in zip(range(0, n, 2), range(1, n, 2)):
            if s[i] != s[j]:
                cnt += 1

        return cnt

class Solution:
    def minChanges(self, s: str) -> int:

        cnt = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                cnt += 1
        return cnt










        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
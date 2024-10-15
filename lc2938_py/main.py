
class Solution:
    def minimumSteps(self, s: str) -> int:

        p1 = 0
        while p1 < len(s) and s[p1] == '0':
            p1 += 1

        p2 = p1
        cnt = 0
        while p2 < len(s):
            if s[p2] == '0':
                cnt += p2 - p1
                p1 += 1
            p2 += 1

        return cnt

class Solution1:
    def minimumSteps(self, s: str) -> int:
        res, swaps = 0, 0
        for ch in s:
            if ch == '1':
                swaps += 1
            else:
                res += swaps

        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
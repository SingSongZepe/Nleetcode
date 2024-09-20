


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        rs = s[::-1]

        for i in range(len(s)):
            if s.startswith(rs[i:]):
                return rs[:i] + s

        return "What the fuck!"


class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        for j in range(n):
            if s[i] == s[n-j-1]:
                i += 1

        if i == n:
            return s
        p = s[i:n][::-1]
        return p + self.shortestPalindrome(s[:i]) + s[i:]

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
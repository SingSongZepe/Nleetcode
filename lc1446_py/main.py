


class Solution:
    def maxPower(self, s: str) -> int:

        p, m, curr = s[0], 1, 1
        for c in s[1:]:
            if c == p:
                curr += 1
            else:
                m = max(m, curr)
                p = c
                curr = 1

        return max(m, curr)



class Solution1:
    def maxPower(self, s: str) -> int:

        m, curr = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                m = max(m, curr)
                curr = 1

        return max(m, curr)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
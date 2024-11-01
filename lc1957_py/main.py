
class Solution:
    def makeFancyString(self, s: str) -> str:

        ss = ''

        for i in range(len(s)):
            if len(ss) > 1 and s[i] == ss[-2] == ss[-1]:
                continue
            ss += s[i]

        return ss

class Solution1:
    def makeFancyString(self, s: str) -> str:

        ss = [s[0]]
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                ss.append(s[i])

        return ''.join(ss)


class Solution2:
    def makeFancyString(self, s: str) -> str:

        ss = [s[0]]
        count = 1
        prev = s[0]

        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                count = 1
            prev = c
            if count < 3:
                ss.append(c)

        return ''.join(ss)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
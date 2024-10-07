
class Solution:
    def minLength(self, s: str) -> int:
        cnt, stack = 0, []
        for c in s:
            if c == 'A':
                stack.append(1)
            elif c == 'C':
                stack.append(-1)
            elif c == 'B':
                if stack and stack[-1] == 1:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(0)
            elif c == 'D':
                if stack and stack[-1] == -1:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(0)
            else:
                stack.append(0)

        return len(s) - cnt


class Solution1:
    def minLength(self, s: str) -> int:
        s1 = []
        for p in s:
            if s1 and ((s1[-1] == "A" and p == "B") or (s1[-1] == "C" and p == "D")):
                s1.pop()
            else:
                s1.append(p)

        return len(s1)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
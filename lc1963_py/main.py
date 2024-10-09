
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        close = 0
        p = len(s) - 1

        for i, c in enumerate(s):
            if c == ']':
                close += 1
                if close > 0:
                    while p > i:
                        p -= 1
                        if s[p+1] == '[':
                            cnt += 1
                            close -= 2
                            break
            else:  # c == '['
                close -= 1

            if i >= p:
                break

        return cnt

class Solution1:
    def minSwaps(self, s: str) -> int:

        unpaired = 0

        for c in s:
            if c == '[':
                unpaired += 1
            elif unpaired > 0:
                unpaired -= 1

        return (unpaired + 1) // 2

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
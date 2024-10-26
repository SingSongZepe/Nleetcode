

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        p1, p2 = 0, 0
        chars.append(' ')
        n = len(chars)
        lst = -1

        def replace(s: int, length: int) -> int:
            length = str(length)
            for c in length:
                chars[s] = c
                s += 1
            return s

        while p2 < n-1:
            if chars[p2] != chars[p2+1]:
                chars[p1] = chars[p2]
                if p2 - lst == 1:
                    p1 += 1
                else:
                    p1 = replace(p1 + 1, p2 - lst)

                lst = p2

            p2 += 1

        return p1











        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
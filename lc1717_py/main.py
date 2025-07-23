

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        s += '#'

        if x >= y: # ab > ba
            c1 = 'a'
            c2 = 'b'
        else:
            c1 = 'b'
            c2 = 'a'
            x, y = y, x

        cnt1, cnt2 = 0, 0
        mark = 0
        for c in s:
            if c == c2:
                if cnt1 > 0:
                    cnt1 -= 1
                    mark += x
                else:
                    cnt2 += 1
            elif c == c1:
                cnt1 += 1
            else:
                mark += y * min(cnt1, cnt2)
                cnt1, cnt2 = 0, 0

        return mark


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
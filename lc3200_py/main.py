

from math import sqrt

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def f1(n) -> int:
            return int(sqrt(4*n)-1)
        def f2(n) -> int:
            return int(sqrt(4*n+1))

        def f3(n) -> int:
            return int(2*sqrt(n))
        def f4(n) -> int:
            return int(sqrt(4*n+1)-1)

        # case 1 n odd, red odd, blue even
        nr1 = f1(red)
        nb1 = f2(blue)
        n1 = min(nr1, nb1)

        # case 2 n odd, red even, blue odd
        nr2 = f1(blue)
        nb2 = f2(red)
        n2 = min(nr2, nb2)

        # case 3 n even, red odd, blue even
        nr3 = f3(red)
        nb3 = f4(blue)
        n3 = min(nr3, nb3)

        # case 4 n even, red even, blue odd
        nr4 = f3(blue)
        nb4 = f4(red)
        n4 = min(nr4, nb4)

        return max(n1, n2, n3, n4)


class Solution1:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def f1(n) -> int:
            return int(sqrt(4*n)-1)
        def f2(n) -> int:
            return int(sqrt(4*n+1))

        def f3(n) -> int:
            return int(2*sqrt(n))
        def f4(n) -> int:
            return int(sqrt(4*n+1)-1)

        return max(min(f1(red), f2(blue)), min(f1(blue), f2(red)), min(f3(red), f4(blue)), min(f3(blue), f4(red)))

class Solution2:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(
            min(int(sqrt(4 * red)) - 1, int(sqrt(4 * blue + 1))),
            min(int(sqrt(4 * blue)) - 1, int(sqrt(4 * red + 1))),
            min(int(2 * sqrt(red)), int(sqrt(4 * blue + 1)) - 1),
            min(int(2 * sqrt(blue)), int(sqrt(4 * red + 1)) - 1)
        )

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
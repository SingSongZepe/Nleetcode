


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 3)
        if m == 0:
            return 1
        elif m == 1:
            return [2, 3, 4][n - 1]
        elif m == 2:
            return [2, 4, 7][n - 1]
        else:
            return [2, 4, 8][n - 1]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
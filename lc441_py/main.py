
from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2*n+0.25) - 0.5)


        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List
from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for W in range(int(sqrt(area)), 0, -1):
            if area % W == 0:
                return [area // W, W]
        return [area, 1]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
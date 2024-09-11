

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x2-x1)*(y3-y2) != (x3-x2)*(y2-y1)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y2-y1)*(x-x1) != (y-y1)*(x2-x1):
                return False

        return True

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x1 == x2: # vertical line
            for x, y in coordinates[2:]:
                if x != x1:
                    return False
        elif y1 == y2: # horizontal line
            for x, y in coordinates[2:]:
                if y != y1:
                    return False
        else:  # slope of line
            v1 = (y2 - y1)
            v2 = (x2 - x1)
            for x, y in coordinates[2:]:
                if v1 * (x - x1) != (y - y1) * v2:
                    return False

        return True


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
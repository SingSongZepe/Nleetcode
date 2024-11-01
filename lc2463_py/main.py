

from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()

        m = len(robot)
        n = len(factory)

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                pass









        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
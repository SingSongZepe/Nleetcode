

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str | int]) -> int:

        for i in range(len(timePoints)):
            h, m = map(int, timePoints[i].split(':'))
            timePoints[i] = h*60 + m

        timePoints.sort()
        timePoints.append(timePoints[0] + 24*60)

        min_diff = float('inf')
        for i in range(len(timePoints)-1):
            diff = timePoints[i+1] - timePoints[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff

class Solution1:
    def findMinDifference(self, timePoints: List[str | int]) -> int:

        def convert_to_minutes(time_str):
            h, m = map(int, time_str.split(':'))
            return h*60 + m

        s = set()
        minutes = []

        for tp in timePoints:
            m = convert_to_minutes(tp)
            if m in s:
                return 0
            s.add(m)
            minutes.append(m)

        minutes.sort()
        minutes.append(minutes[0] + 24*60)
        min_diff = float('inf')
        for i in range(len(minutes)-1):
            diff = minutes[i+1] - minutes[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
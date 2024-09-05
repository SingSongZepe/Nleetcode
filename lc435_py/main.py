

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                prev = min(prev, intervals[i][1])
                count += 1

        return count



def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(startTime[i] <= queryTime <= endTime[i] for i in range(len(startTime)))


class Solution1:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        cnt = 0
        for s, e in zip(startTime, endTime):
            cnt += s <= queryTime <= e

        return cnt

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
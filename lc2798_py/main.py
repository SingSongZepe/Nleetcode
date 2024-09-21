

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        return sum(1 for h in hours if h >= target)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
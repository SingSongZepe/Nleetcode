

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = (len(rolls) + n) * mean - sum(rolls)

        if target < n or target > 6*n:
            return []

        ave = target // n
        remainder = target % n

        return [ave] * (n - remainder) + [ave + 1] * remainder

def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return [num for num in [min(row) for row in matrix] if num in set([max(col) for col in zip(*matrix)])]





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
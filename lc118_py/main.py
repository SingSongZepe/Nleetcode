

from typing import List

class Solution:
    def generate(self, nr: int) -> List[List[int]]:
        if nr == 1:
            return [[1]]
        elif nr == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for i in range(2, nr):
            line = [1] * (i+1)
            for j in range(1, i):
                line[j] = res[i-1][j-1] + res[i-1][j]
            res.append(line)

        return res



class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
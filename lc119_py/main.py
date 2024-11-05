

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = [1]
        for i in range(1, rowIndex//2+1):
            res.append(res[-1] * (rowIndex - i + 1) // i)

        if rowIndex % 2: # odd
            res.extend(res[::-1])
        else: # even
            res.extend(res[-2::-1])

        return res















        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
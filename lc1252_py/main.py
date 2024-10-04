

from typing import List

# bit manipulation solution
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mtx = [(1 << n) - 1] * m

        for r, c in indices:
            for i in range(m):
                if i == r:
                    mtx[i] ^= ~(1 << c)
                else:
                    mtx[i] ^= 1 << c

        cnt = 0
        for i in mtx:
            cnt += bin(i & ((1 << n) - 1)).count('1')

        return m*n - cnt


# bit manipulation solution
class Solution1:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_mask = 0
        col_mask = 0

        for r, c in indices:
            row_mask ^= (1 << r)
            col_mask ^= (1 << c)

        odd_count = 0

        for i in range(m):
            for j in range(n):
                is_odd_row = (row_mask & (1 << i)) != 0
                is_odd_col = (col_mask & (1 << j)) != 0
                if is_odd_row ^ is_odd_col:
                    odd_count += 1

        return odd_count

# matrix solution
class Solution2:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_counts = [0] * m
        col_counts = [0] * n

        for r, c in indices:
            row_counts[r] += 1
            col_counts[c] += 1

        odd_count = 0

        for r in range(m):
            for c in range(n):
                if (row_counts[r] + col_counts[c]) % 2 == 1:
                    odd_count += 1

        return odd_count

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
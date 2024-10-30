

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x_ = 'X'
        o_ = 'O'
        any_char_ = '*'
        m, n = len(board), len(board[0])

        dq = []
        for i in range(m):
            if board[i][0] == o_:
                dq.append((i, 0))
            if board[i][n-1] == o_:
                dq.append((i, n-1))

        for i in range(1, n-1):
            if board[0][i] == o_:
                dq.append((0, i))
            if board[m-1][i] == o_:
                dq.append((m-1, i))

        while dq:
            for _ in range(len(dq)):
                r, c = dq.pop()
                board[r][c] = any_char_
                # up
                if r > 1 and board[r-1][c] == o_:
                    dq.append((r-1, c))
                # down
                if r < m-2 and board[r+1][c] == o_:
                    dq.append((r+1, c))
                # left
                if c > 1 and board[r][c-1] == o_:
                    dq.append((r, c-1))
                # right
                if c < n-2 and board[r][c+1] == o_:
                    dq.append((r, c+1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == any_char_:
                    board[i][j] = o_
                else:
                    board[i][j] = x_










def main():
    print('Hello World')

if __name__ == '__main__':
    main()
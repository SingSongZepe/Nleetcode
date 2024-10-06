

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        mp = [[0] * 3 for _ in range(3)]
        for i, move in enumerate(moves):
            if i % 2 == 0:
                mp[move[0]][move[1]] = 1
            else:
                mp[move[0]][move[1]] = -1

        # row and col check
        for i in range(3):
            rsum = sum(mp[i])
            csum = mp[0][i] + mp[1][i] + mp[2][i]
            if rsum == 3 or csum == 3:
                return "A"
            elif rsum == -3 or csum == -3:
                return "B"

        # diagonal check
        dsum = mp[0][0] + mp[1][1] + mp[2][2]
        if dsum == 3:
            return "A"
        elif dsum == -3:
            return "B"

        dsum = mp[0][2] + mp[1][1] + mp[2][0]
        if dsum == 3:
            return "A"
        elif dsum == -3:
            return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
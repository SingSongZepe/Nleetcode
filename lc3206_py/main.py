

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        sm = sum(colors[:2])

        colors += colors[:2]
        vaild = 0

        for cnt_i in range(1, len(colors)-1):
            sm += colors[cnt_i+1]
            if (sm == 1 and colors[cnt_i] == 1) or (sm == 2 and colors[cnt_i] == 0):
                vaild += 1
            sm -= colors[cnt_i-1]

        return vaild



def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:


        ml, mask = 0, 1
        for _ in range(24):
            cl = 0
            for n in candidates:
                if n & mask:
                    cl += 1
            ml = max(ml, cl)
            mask <<= 1

        return ml

















        pass



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
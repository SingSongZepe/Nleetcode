

from typing import List

class Solution:
    def fairCandySwap(self, als: List[int], bos: List[int]) -> List[int]:
        atot, btot = sum(als), sum(bos)
        diff = (atot - btot) // 2
        set_b = set(bos)
        for a in als:
            if a - diff in set_b:
                return [a, a - diff]

        return [0, 0]

class Solution:
    def fairCandySwap(self, als: List[int], bos: List[int]) -> List[int]:



        pass

def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List
from math import log10

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        st = set()

        for n in arr1:
            while n:
                st.add(n)
                n //= 10

        mx = 0
        mv = 0
        for n in arr2:
            if n <= mv:
                continue

            while n:
                if n in st:
                    length = int(log10(n)) + 1
                    if length > mx:
                        mx = length
                        mv = n
                    break
                n //= 10

        return mx

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
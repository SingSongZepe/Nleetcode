

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        res = [0] * n

        sign = 1 if k > 0 else -1
        k = k if k > 0 else -k

        for i in range(n):
            res[i] = sum([code[(i+sign*j)%n] for j in range(1, k+1)])

        return res

class Solution1:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        twice = code + code
        twice = twice if k >= 0 else twice[::-1]
        kk = k if k >= 0 else -k

        for i in range(len(code)):
            code[i] = sum(twice[i+1:i+kk+1])

        return code if k >= 0 else code[::-1]




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
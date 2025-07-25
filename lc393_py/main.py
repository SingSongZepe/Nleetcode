
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        i, n = 0, len(data)

        def start_with_11110(a: int) -> bool:
            return a >= 0b11110000 and a & 0b1000 == 0

        def start_with_1110(a: int) -> bool:
            return a >= 0b11100000 and a & 0b10000 == 0

        def start_with_110(a: int) -> bool:
            return a >= 0b11000000 and a & 0b100000 == 0

        def start_with_10(a: int) -> bool:
            return a >= 0b10000000 and a & 0b1000000 == 0

        def start_with_0(a: int) -> bool:
            return a < 0b10000000

        while i < n:
            if start_with_11110(data[i]):
                for j in range(i+1, i+4):
                    if j >= n or not start_with_10(data[j]):
                        return False
                i += 4
            elif start_with_1110(data[i]):
                for j in range(i+1, i+3):
                    if j >= n or not start_with_10(data[j]):
                        return False
                i += 3
            elif start_with_110(data[i]):
                for j in range(i+1, i+2):
                    if j >= n or not start_with_10(data[j]):
                        return False
                i += 2
            elif start_with_0(data[i]):
                i += 1
            else:
                return False

        return True

# better solution
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def start_with_11110(a: int) -> bool:
            return a >= 0b11110000 and a & 0b1000 == 0

        def start_with_1110(a: int) -> bool:
            return a >= 0b11100000 and a & 0b10000 == 0

        def start_with_110(a: int) -> bool:
            return a >= 0b11000000 and a & 0b100000 == 0

        def start_with_10(a: int) -> bool:
            return a >= 0b10000000 and a & 0b1000000 == 0

        def start_with_0(a: int) -> bool:
            return a < 0b10000000

        num_subbytes = 0

        for n in data:
            if num_subbytes == 0:
                if start_with_11110(n):
                    num_subbytes = 3
                elif start_with_1110(n):
                    num_subbytes = 2
                elif start_with_110(n):
                    num_subbytes = 1
                elif start_with_0(n):
                    pass
                else:
                    return False
            else:
                if not start_with_10(n):
                    return False
                num_subbytes -= 1

        return num_subbytes == 0

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        num_subbytes = 0

        for n in data:
            if num_subbytes == 0:
                if n >> 3 == 0b11110:
                    num_subbytes = 3
                elif n >> 4 == 0b1110:
                    num_subbytes = 2
                elif n >> 5 == 0b110:
                    num_subbytes = 1
                elif n >> 7 != 0b0:
                    return False
            else:
                if not n >> 6 == 0b10:
                    return False
                num_subbytes -= 1

        return num_subbytes == 0




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
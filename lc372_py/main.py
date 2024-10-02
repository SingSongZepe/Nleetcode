

from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        def right_shift(b: List[int]) -> List[int]:
            for i in range(len(b)-1, 0, -1):
                b[i] = b[i] // 2 + (5 if b[i-1] % 2 == 1 else 0)
            b[0] = b[0] // 2
            return b

        def check_empty_list(b: List[int]) -> bool:
            return sum(b) == 0

        if a == 1:
            return 1

        r = 1
        a %= 1337
        while not check_empty_list(b):
            if b[-1] % 2 == 1:
                r = (r * a) % 1337
            a = (a * a) % 1337
            b = right_shift(b)
        return r


class Solution1:
    MOD = 1337

    def pow(self, a: int, b: int) -> int:
        result = 1
        a %= self.MOD  # Taking mod to prevent overflow
        for _ in range(b):
            result = (result * a) % self.MOD
        return result

    def superPow(self, a: int, b: list[int]) -> int:
        result = 1
        for i in range(len(b) - 1, -1, -1):
            result = (result * self.pow(a, b[i])) % self.MOD
            a = self.pow(a, 10)  # Power up for the next iteration
        return result


class Solution2:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1

        a %= 1337
        temp = a * a
        cycle_len = 1
        while temp != a:
            temp = (temp * a) % 1337
            cycle_len += 1

        remainder = 0
        for i in range(len(b)):
            remainder = (remainder * 10 + b[i]) % cycle_len

        if remainder == 0:
            remainder = cycle_len  # there is not 'a', it's the last element of the cycle

        result = 1
        for i in range(remainder):
            result = (result * a) % 1337
        return result


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
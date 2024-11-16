

from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        total: int = 0
        ones = zeros = 0
        left: int = 0

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1
            else:
                zeros += 1

            while ones > k and zeros > k:
                if s[left] == '1':
                    ones -= 1
                else:
                    zeros -= 1
                left += 1

            total += right - left + 1

        return total










        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
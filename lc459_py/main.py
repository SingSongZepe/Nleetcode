
from math import sqrt, ceil

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        if len(s) == 1:
            return False

        # optimized force brute
        n = len(s)
        for leng in range(1, n // 2 + 1):
            if n % leng == 0:
                pattern = s[:leng]
                if all(s[leng*i:leng*(i+1)] == pattern for i in range(1, n // leng)):
                    return True

        return False

# a tricky solution
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
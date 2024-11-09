
class Solution:
    def minEnd(self, n: int, x: int) -> int:

        curr_mask = 1
        n -= 1
        while n:
            if not x & curr_mask:
                x ^= curr_mask if n & 1 else 0
                n >>= 1
            curr_mask <<= 1

        return x



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
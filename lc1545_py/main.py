
class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def make(s: str, n: int) -> str:
            if n == 0:
                return '0'

            new = make(s, n-1)
            return new + '1' + ''.join(reversed(['1' if x == '0' else '0' for x in new]))

        return make('0', n-1)[k-1]

class Solution1:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        mid = (1 << n) // 2

        if k < mid:
            return self.findKthBit(n - 1, k)
        elif k == mid:
            return "1"
        else:
            corresponding_bit = self.findKthBit(n - 1, (1 << n) - k)
            return "1" if corresponding_bit == "0" else "0"





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
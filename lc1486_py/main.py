


class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        x = start
        for i in range(1, n):
            x ^= start + 2 * i

        return x




        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
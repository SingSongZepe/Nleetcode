
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n << 1


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
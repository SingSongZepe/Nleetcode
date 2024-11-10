
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        n, xx = 0, x
        while xx:
            n += xx % 10
            xx //= 10

        return -1 if x % n else n





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
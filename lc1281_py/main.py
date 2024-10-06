


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n:
            digit = n % 10
            product *= digit
            sum += digit
            n //= 10
        return product - sum



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
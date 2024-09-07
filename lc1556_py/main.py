


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'

        buffer, sp = '', 0

        while n > 0:
            buffer = str(n % 10) + buffer
            n //= 10
            sp += 1
            if sp % 3 == 0 and sp != 0 and n > 0:
                buffer = '.' + buffer

        return buffer



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
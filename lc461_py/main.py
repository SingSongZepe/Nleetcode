
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
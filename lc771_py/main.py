


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in set(jewels))


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
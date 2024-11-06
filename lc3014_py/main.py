
class Solution:
    def minimumPushes(self, word: str) -> int:
        return len(word) if len(word) < 9 else (2 * len(word) - 8 if len(word) < 17 else (3 * len(word) - 24 if len(word) < 25 else 4 * len(word) - 48))










        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        def hash(c: str) -> int:
            if c == 'b':
                return 0
            elif c == 'a':
                return 1
            elif c == 'l':
                return 2
            elif c == 'o':
                return 3
            elif c == 'n':
                return 4

        freq = [0] * 5
        for c in text:
            if c in 'balon':
                freq[hash(c)] += 1

        return min(freq[0], freq[1], freq[2] // 2, freq[3] // 2, freq[4])



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
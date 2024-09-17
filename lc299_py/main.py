

from typing import List
from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0
        cows = 0
        unmatched = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                continue

            s = int(s)
            g = int(g)
            if unmatched[s] < 0:
                cows += 1
            if unmatched[g] > 0:
                cows += 1
            unmatched[s] += 1
            unmatched[g] -= 1

        return f"{bulls}A{cows}B"




class Solution1:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        raj = [0] * 10

        for i in range(len(secret)):
            sec = int(secret[i])
            gu = int(guess[i])

            if sec == gu:
                bulls += 1
                continue
            if raj[sec] < 0:
                cows += 1
            if raj[gu] > 0:
                cows += 1
            raj[sec] += 1
            raj[gu] -= 1

        return f"{bulls}A{cows}B"


from collections import Counter

class Solution2:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0

        h = Counter(secret)
        cows = 0

        for i, ch in enumerate(guess):
            if ch in h:
                if ch == secret[i]:
                    bulls += 1
                    # print(h[ch] <= 0)
                    cows -= int(h[ch] <= 0)
                else:
                    cows += int(h[ch] > 0)
                h[ch] -= 1

        return "{}A{}B".format(bulls, cows)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
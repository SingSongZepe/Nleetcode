

from typing import List

from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        d = defaultdict(list[int])

        for v in votes:
            for i, c in enumerate(v):
                if c not in d:
                    d[c] = [0] * n
                d[c][i] += 1

        return ''.join(sorted(d.keys(), key=lambda x: d[x], reverse=True))




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
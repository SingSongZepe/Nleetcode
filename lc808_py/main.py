

from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        return self.serve(n, n) if n < 5000 else 1.0

    # DP, pure function
    @cache
    def serve(self, a: int, b: int) -> float:
        match a <= 0, b <= 0:
            case True, True: return 0.5
            case True, False: return 1.0
            case False, True: return 0.0
            # continue with the recursive case
            case False, False: return \
                sum(self.serve(a - da, b - db) for da, db in [(100, 0), (75, 25), (50, 50), (25, 75)]
            ) / 4


from math import ceil

class Solution1:
    def soupServings(self, n: int) -> float:
        n = ceil(n / 25)
        return self.serve(n, n) if n < 200 else 1.0

    # DP, pure function
    @cache
    def serve(self, a: int, b: int) -> float:
        match a <= 0, b <= 0:
            case True, True: return 0.5
            case True, False: return 1.0
            case False, True: return 0.0
            # continue with the recursive case
            case False, False: return \
                sum(self.serve(a - da, b - db) for da, db in [(4, 0), (3, 1), (2, 2), (1, 3)]
            ) / 4


# DP, recursive, hardcored saturation point
def serve(soupA, soupB, lookup):
    if (soupA, soupB) in lookup:
        return lookup[(soupA, soupB)]
    if soupA <= 0 and soupB <= 0:
        return 0.5
    if soupA <= 0:
        return 1
    if soupB <= 0:
        return 0

    lookup[(soupA, soupB)] = 0.25 * (
                serve(soupA - 100, soupB - 0, lookup) +
                serve(soupA - 75, soupB - 25, lookup) +
                serve(soupA - 50, soupB - 50, lookup) +
                serve(soupA - 25, soupB - 75, lookup)
    )
    return lookup[(soupA, soupB)]


class Solution2:
    def soupServings(self, n: int) -> float:
        lookup = {}
        if n > 4800: # hardcored saturation point
            return 1.0
        return serve(n, n, lookup)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
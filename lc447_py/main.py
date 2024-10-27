

from typing import List, Set, Tuple, Dict
from math import sqrt
from collections import defaultdict


# misunderstanding
# I thought that this question require equal distance and on-a-line point pairs
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        vspace: Set[Tuple[int, int]] = set()

        for x, y in points:
            vspace.add((x, y))

        pairs = 0
        for ix, iy in points:
            for (jx, jy) in vspace:
                if jx == ix and jy == iy:
                    continue
                kx, ky = 2 * ix - jx, 2 * iy - jy
                if (kx, ky) in vspace:
                    pairs += 1

        return pairs


class Solution1:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        pairs = 0

        for p1 in points:
            d: Dict[int, int] = {}
            for p2 in points:
                dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                if dist in d:
                    pairs += 2 * d[dist]
                    d[dist] += 1
                else:
                    d[dist] = 1

        return pairs



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
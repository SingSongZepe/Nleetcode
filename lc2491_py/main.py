

from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        cnt = Counter(skill)
        tot = min(skill) + max(skill)
        res = 0
        st = set(skill)

        for n in st:
            if n == tot / 2:
                if cnt[n] % 2 == 1:
                    return -1
                else:
                    res += cnt[n] * n * n
            else:
                if cnt[n] != cnt[tot - n]:
                    return -1
                else:
                    res += cnt[n] * n * (tot - n)

        return res // 2

class Solution1:
    def dividePlayers(self, skill: List[int]) -> int:
        cnt = Counter(skill)
        tot = min(skill) + max(skill)
        res = 0
        st = set(skill)

        for n in st:
            if cnt[n] != cnt[tot - n]:
                return -1
            res += cnt[n] * n * (tot - n)

        return res // 2


class Solution2:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot = skill[-1] + skill[0]
        l, r = 0, len(skill) - 1
        res = 0
        while l < r:
            if skill[l] + skill[r] != tot:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1

        return res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
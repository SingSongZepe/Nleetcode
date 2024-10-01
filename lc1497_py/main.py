

from typing import List, Mapping

from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt: Mapping[int, int] = Counter([n % k for n in arr])

        if cnt[0] % 2 == 1:
            return False
        for i in range(1, (k + 1) // 2):
            if cnt[i] != cnt[k - i]:
                return False
        return True


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
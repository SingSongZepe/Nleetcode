

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        cnter = Counter(s)
        tar_cnter = Counter(target)

        min_cnt = 100
        for c, cnt in tar_cnter.items():
            if c not in cnter:
                return 0
            min_cnt = min(min_cnt, cnter[c] // cnt)

        return min_cnt




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
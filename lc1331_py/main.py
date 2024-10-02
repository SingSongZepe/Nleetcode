

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        b = sorted(set(arr))
        c = {ele: rank + 1 for rank, ele in enumerate(b)}
        ranked_arr = [c[ele] for ele in arr]
        return ranked_arr


def main():
    print('Hello World')

if __name__ == '__main__':
    main()

from typing import List, Tuple
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:

        cnt = Counter(s)
        sorted_count = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

        res = ''
        for c, freq in sorted_count:
            res += freq * c

        return res




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
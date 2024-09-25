

from typing import List
import heapq

from collections import Counter
from heapq import *



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, (-freq, word))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res




class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = Counter(words)

        max_freq = max(freq_dict.values())

        buckets = [[] for _ in range(max_freq + 1)]

        for key, val in freq_dict.items():
            heappush(buckets[val], key)

        ans = []
        bucket_index = max_freq
        while k > 0:
            if len(buckets[bucket_index]) > 0:
                ans.append(heappop(buckets[bucket_index]))
                k -= 1
            else:
                bucket_index -= 1

        return ans


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        heap = []
        for word, freq in word_freq.items():
            heapq.heappush(heap, (-freq, word))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
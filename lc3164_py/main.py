import bisect
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        cnt = 0
        st1 = set()
        pairs = set()
        for n1 in nums1:
            if n1 in st1:
                continue
            if n1 % k != 0:
                st1.add(n1)
                continue
            n1 //= k
            for n2 in nums2:
                if (n1, n2) in pairs:
                    cnt += 1
                    continue
                if n1 % n2 == 0:
                    cnt += 1
                    pairs.add((n1, n2))

        return cnt


from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        cnt = 0

        d1 = Counter(nums1)
        d2 = Counter(nums2)
        nums2 = sorted(d2.keys())

        for n1, c1 in d1.items():
            if n1 % k != 0:
                continue
            n1 //= k

            r = bisect.bisect_left(nums2, n1)
            if n1 == nums2[r]:
                r += 1
            for i in range(r):
                if n1 % nums2[i] == 0:
                    cnt += d2[nums2[i]]


        return cnt

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        cnt = 0
        d1 = Counter(nums1)
        m1 = max(d1)
        d2 = Counter(nums2)

        for n2, c2 in d2.items():
            divisor = n2 * k
            curr = divisor

            if divisor == 1:
                cnt += len(nums1)
                continue

            while curr <= m1:
                if curr in d1:
                    cnt += c2 * d1[curr]
                curr += divisor

        return cnt








def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        st1 = set(nums1)
        overlap = 10
        for n2 in nums2:
            if n2 in st1 and overlap > n2:
                overlap = n2

        if overlap < 10:
            return overlap

        m1, m2 = min(nums1), min(nums2)
        if m1 > m2:
            m1, m2 = m2, m1
        return m1 * 10 + m2




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
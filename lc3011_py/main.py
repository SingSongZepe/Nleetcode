

from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        prev_m = None
        curr_m = nums[0]
        curr_cnt = nums[0].bit_count()
        for n in nums[1:]:
            if n.bit_count() == curr_cnt:
                if prev_m and n < prev_m:
                    return False
                if n > curr_m:
                    curr_m = n
            else:
                curr_cnt = n.bit_count()
                prev_m = curr_m
                curr_m = n
                if prev_m and n < prev_m:
                    return False

        return True if prev_m is None or curr_m > prev_m else False




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
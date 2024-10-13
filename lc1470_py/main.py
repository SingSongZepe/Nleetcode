

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        res = [0] * (2*n)

        for i in range(n):
            res[2*i] = nums[i]
            res[2*i+1] = nums[i+n]

        return res


# bit manipulation
# store two data in one integer, but the data can not be larger than 2^10 - 1
class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(0, n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]

        for i in range(n, 0, -1):
            first = nums[i - 1] >> 10
            second = nums[i - 1] & 0b1111111111
            nums[2 * i - 1] = second
            nums[2 * i - 2] = first
        return nums


class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        des = 1
        tmp = nums[des]

        while True:
            if des < n:
                to = 2 * des
            else:
                to = 2 * (des - n) + 1

            if des == to:
                break

            tmp = nums[to]
            nums[to] = tmp
            des = to


        return nums



def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List
from math import sqrt


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        st = set()
        res = []

        for n in nums:
            if n in st:
                res.append(n)
            else:
                st.add(n)

        return res


class Solution1:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums) - 2

        exp_tot_1 = n * (n + 1) // 2
        exp_tot_2 = n * (n + 1) * (2 * n + 1) // 6

        tot_1, tot_2 = 0, 0
        for num in nums:
            tot_1 += num
            tot_2 += num * num

        diff_1 = exp_tot_1 - tot_1
        diff_2 = exp_tot_2 - tot_2
        s = sqrt(diff_2 - 3 / 4 * diff_1 * diff_1)

        return [int(s + 1/2*diff_1), int(1/2*diff_1-s)]

class Solution2:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums) - 2

        sum_expected = (n * (n - 1)) // 2
        sum_actual = sum(nums)

        sum_squares_expected = (n * (n - 1) * (2 * n - 1)) // 6
        sum_squares_actual = sum(x * x for x in nums)

        S = sum_actual - sum_expected  # M + N
        P = (sum_squares_actual - sum_squares_expected) // S  # M * N

        # Checks for valid discrimination
        discriminant = S * S - 4 * P

        if discriminant < 0:
            raise ValueError("No real roots found. Please check the input data.")

        sqrt_discriminant = int(discriminant ** 0.5)

        M = (S + sqrt_discriminant) // 2
        N = (S - sqrt_discriminant) // 2

        # Validate that M and N are indeed in the range [0, n-1]
        if 0 <= M < n and 0 <= N < n:
            return [M, N]
        else:
            raise ValueError("M or N is out of the expected range.")

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
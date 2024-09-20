

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        tn = n * n

        s = tn * (tn + 1) // 2
        sqr_s = tn * (tn + 1) * (2 * tn + 1) // 6

        act_s = sum(sum(row) for row in grid)
        act_sqr_s = sum(sum(num * num for num in row) for row in grid)

        diff = act_s - s
        diff_sqr = act_sqr_s - sqr_s

        return [(diff + diff_sqr // diff) // 2, (diff_sqr // diff - diff) // 2]
        pass

def find_repeating_and_missing(grid):
    n = len(grid)

    # Calculate expected sums
    total_numbers = n * n
    expected_sum = total_numbers * (total_numbers + 1) // 2
    expected_square_sum = total_numbers * (total_numbers + 1) * (2 * total_numbers + 1) // 6

    # Calculate actual sums
    actual_sum = 0
    actual_square_sum = 0

    for row in grid:
        for num in row:
            actual_sum += num
            actual_square_sum += num * num

            # Set up the equations
    diff_sum = expected_sum - actual_sum  # b - a
    diff_square_sum = expected_square_sum - actual_square_sum  # b^2 - a^2

    # We have:
    # diff_square_sum = (b - a)(b + a) = diff_sum * (b + a)
    # => b + a = diff_square_sum / diff_sum

    b_plus_a = diff_square_sum // diff_sum

    # Now we can solve for b and a
    a = (b_plus_a - diff_sum) // 2
    b = a + diff_sum

    return [a, b]

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
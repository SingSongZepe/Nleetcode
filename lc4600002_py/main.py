
class Solution:
    def numOfSubsequences(self, s: str):
        n = len(s)
        prefix_L = [0] * (n + 1)
        prefix_C = [0] * (n + 1)

        for i in range(n):
            prefix_L[i + 1] = prefix_L[i] + (1 if s[i] == 'L' else 0)
            prefix_C[i + 1] = prefix_C[i] + (1 if s[i] == 'C' else 0)

        suffix_C = [0] * (n + 1)
        suffix_T = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_C[i] = suffix_C[i + 1] + (1 if s[i] == 'C' else 0)
            suffix_T[i] = suffix_T[i + 1] + (1 if s[i] == 'T' else 0)

        current_count = 0
        for j in range(n):
            if s[j] == 'C':
                left_L = prefix_L[j]
                right_T = suffix_T[j]
                current_count += left_L * right_T

        max_count = 0

        for i in range(n + 1):
            count_LCT_with_L = suffix_C[i] * suffix_T[i]
            max_count = max(max_count, count_LCT_with_L)

            count_LCT_with_C = prefix_L[i] * suffix_T[i]
            max_count = max(max_count, count_LCT_with_C)

            count_LCT_with_T = prefix_L[i] * prefix_C[i]
            max_count = max(max_count, count_LCT_with_T)

        return max_count + current_count


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
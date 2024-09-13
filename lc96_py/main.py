
class Solution:
    def numTrees(self, n: int) -> int:

        dp = {}

        def g(start: int, end: int) -> int:
            if (start, end) in dp:
                return dp[(start, end)]
            if start > end:
                return 1

            dp[(start, end)] = sum([g(start, i-1) * g(i+1, end) for i in range(start, end+1)])
            return dp[(start, end)]


        return g(1, n)


class Solution1:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        num_trees = [0 for _ in range(n + 1)]
        num_trees[0] = 1
        num_trees[1] = 1
        num_trees[2] = 2

        for i in range(3, n + 1):
            cur_num = 0
            for j in range(1, i + 1):
                cur_num += num_trees[j - 1] * num_trees[i - j]
            num_trees[i] = cur_num
            # print(cur_num)

        return num_trees[-1]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
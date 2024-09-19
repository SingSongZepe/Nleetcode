
from typing import List

from functools import cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @cache
        def dfs(expr: str) -> List[int]:
            if len(expr) == 0: # empty string
                return []

            if expr.isnumeric(): # a number
                return [int(expr)]

            # splitting into two parts and dfs
            result = []
            for i, c in enumerate(expr):
                if c in '+-*':
                    lr = dfs(expr[:i])
                    rl = dfs(expr[i+1:])
                    for l in lr:
                        for r in rl:
                            if c == '+':
                                result.append(l + r)
                            elif c == '-':
                                result.append(l - r)
                            elif c == '*':
                                result.append(l * r)
            return result
        return dfs(expression)




class Solution1:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub_str1 = expression[0:i]
                sub_str2 = expression[i+1:]
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                for i in s1:
                    for j in s2:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(expression))

        return res


class Solution2:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @cache
        def dfs(expr):
            if len(expr) == 0:
                return []

            if expr.isnumeric():
                return [int(expr)]

            result = []
            for i, c in enumerate(expr):
                if c.isdigit():
                    continue
                left_result = dfs(expr[:i])
                right_result = dfs(expr[i + 1:])

                for lr in left_result:
                    for rl in right_result:
                        match c:
                            case '+':
                                result.append(lr + rl)
                            case '-':
                                result.append(lr - rl)
                            case '*':
                                result.append(lr * rl)

            return result

        return dfs(expression)



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
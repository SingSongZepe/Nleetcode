

from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        op_stack: List[str] = []             # [ &, !, |, ...]
        bool_stack: List[List[bool]] = []    # [[True, False], [True, False]]
        current: List[bool] = []             # [True, False]

        p, n = 0, len(expression)
        while p < n:
            c = expression[p]
            if c in '!|&':
                op_stack.append(c)
                bool_stack.append(current)
                current = []

            elif c == 't':
                current.append(True)
                if op_stack[-1] == '|':
                    while p < n and expression[p] != ')':
                        p += 1
                    continue

            elif c == 'f':
                current.append(False)
                if op_stack[-1] == '&':
                    while p < n and expression[p] != ')':
                        p += 1
                    continue

            elif c == ')':
                if op_stack[-1] == '|':
                    rb = any(reversed(current))
                elif op_stack[-1] == '&':
                    rb = all(reversed(current))
                else:
                    rb = not current[0]

                bool_stack.pop()
                if bool_stack:
                    bool_stack[-1].append(rb)
                else:
                    bool_stack.append([rb])
                current = bool_stack[-1]

                op_stack.pop()

            p += 1

        return bool_stack[0][0]

class Solution1:
    def parseBoolExpr(self, expression: str) -> bool:
        op_stack: List[str] = []             # [ &, !, |, ...]
        bool_stack: List[List[bool]] = []    # [[True, False], [True, False]]

        p, n = 0, len(expression)

        while p < n:
            c = expression[p]
            if c in '(,':
                pass
            elif c in '|&!':
                op_stack.append(c)
                bool_stack.append([])
            elif c == 't':
                bool_stack[-1].append(True)
                if op_stack[-1] == '|':
                    while p < n and expression[p] != ')':
                        p += 1
                    continue
            elif c == 'f':
                bool_stack[-1].append(False)
                if op_stack[-1] == '&':
                    while p < n and expression[p] != ')':
                        p += 1
                    continue
            else:  # ')'
                current = bool_stack.pop()
                if op_stack[-1] == '&':
                    rb = all(reversed(current))
                elif op_stack[-1] == '|':
                    rb = any(reversed(current))
                else:  # '!'
                    rb = not current[0]

                if bool_stack:
                    bool_stack[-1].append(rb)
                else:
                    bool_stack.append([rb])

                op_stack.pop()

            p += 1

        return bool_stack[0][0]



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
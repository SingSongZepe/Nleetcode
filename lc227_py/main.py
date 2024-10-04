

# Fake Solution
# the order of processing the stack errors
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        op_stack = []
        n = 0
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c in '+-*/':
                if op_stack and op_stack[-1] in '*/':
                    match op_stack.pop():
                        case '*':
                            stack.append(stack.pop() * n)
                        case '/':
                            stack.append(int(stack.pop() / n))
                else:
                    stack.append(n)
                n = 0
                op_stack.append(c)

        stack.append(n)
        while op_stack:
            match op_stack.pop():
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    v = stack.pop()
                    stack.append(stack.pop() - v)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    v = stack.pop()
                    stack.append(int(stack.pop() / v))

        return stack[-1]


class Solution1:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_operator = '+'

        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))

                prev_operator = ch
                num = 0

        return sum(stack)



class Solution2:
    def calculate(self, s: str) -> int:
        sign, num = "+", 0
        stack = []
        for i in s+"+":
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in '+-/*':
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = i
                num = 0

        return sum(stack)



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
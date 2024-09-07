
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        res = ''.join(stack[:-k] if k > 0 else stack).lstrip('0')
        return res if res else '0'










        pass



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
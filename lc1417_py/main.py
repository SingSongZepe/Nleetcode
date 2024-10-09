

class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        digits = []

        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                chars.append(c)

        if len(chars) > len(digits):
            chars, digits = digits, chars

        m, n = len(chars), len(digits)
        if abs(m - n) > 1:
            return ""


        result = []
        for i in range(m):
            result.append(chars[i] + chars[i])

        if m < n:
            result.append(digits[-1])

        return ''.join(result)



def main():
    print('Hello World')

if __name__ == '__main__':
    main()

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        open = 0
        close = 0

        for c in s:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    close += 1

        return open + close





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
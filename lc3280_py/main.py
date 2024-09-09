


class Solution:
    def convertDateToBinary(self, date: str) -> str:

        y, m, d = map(int, date.split('-'))
        return bin(y)[2:] + '-' + bin(m)[2:] + '-' + bin(d)[2:]



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
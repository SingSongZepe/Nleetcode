



class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        corr_h, corr_m = map(int, correct.split(':'))
        corr = corr_h * 60 + corr_m
        curr_h, curr_m = map(int, current.split(':'))
        curr = curr_h * 60 + curr_m

        diff = corr - curr

        cnt = 0

        cnt += diff // 60
        diff %= 60

        cnt += diff // 15
        diff %= 15

        cnt += diff // 5
        diff %= 5

        return cnt + diff



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
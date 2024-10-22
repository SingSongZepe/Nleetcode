

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:

        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)






def main():
    print('Hello World')

if __name__ == '__main__':
    main()
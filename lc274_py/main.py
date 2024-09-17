

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        count = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                count += 1
            else:
                break

        return count

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
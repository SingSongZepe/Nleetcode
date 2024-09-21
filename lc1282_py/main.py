
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}

        for i, s in enumerate(groupSizes):
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)

        result = []
        for k in d:
            for i in range(0, len(d[k]), k):
                result.append(d[k][i:i+k])

        return result




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
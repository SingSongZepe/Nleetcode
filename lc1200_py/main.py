

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi = float('inf')
        pairs = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < mi:
                mi = arr[i+1] - arr[i]
                pairs = [[arr[i], arr[i+1]]]
            elif arr[i+1] - arr[i] == mi:
                pairs.append([arr[i], arr[i+1]])
        return pairs



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
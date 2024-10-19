

from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        for i in range(len(arr)-m*k+1):
            pattern = arr[i:i+m]
            match = True
            for j in range(k):
                if arr[i+j*m:i+(j+1)*m] != pattern:
                    match = False
                    break

            if match:
                return True

        return False






        pass



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
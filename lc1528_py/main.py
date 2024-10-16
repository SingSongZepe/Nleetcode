

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        res = [''] * len(s)

        for i in range(len(s)):
            res[indices[i]] = s[i]

        return ''.join(res)




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
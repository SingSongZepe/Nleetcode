import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sortedArrayToBST(arg)
        print(result)
        
    def test1(self):
        nums = [-10, -3, 0, 5, 9]
        self.t(nums)

    def test2(self):
        nums = [1, 3]
        self.t(nums)

if __name__ == '__main__':
    unittest.main()
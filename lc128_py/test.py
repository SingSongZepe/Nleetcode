import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestConsecutive(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [100,4,200,1,3,2]
        expected = 4
        self.t(nums, expected)

    def test2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        self.t(nums, expected)




if __name__ == '__main__':
    unittest.main()
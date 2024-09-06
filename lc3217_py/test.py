import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, head, expected=None):
        result = Solution().modifiedList(nums, head)
        print_list(result)
        
    def test1(self):
        nums = [1, 2, 3]
        head = build_list([1, 2, 3, 4, 5])
        self.t(nums, head)

    def test2(self):
        nums = [1]
        head = build_list([1, 2, 1, 2, 1, 2])
        self.t(nums, head)

if __name__ == '__main__':
    unittest.main()
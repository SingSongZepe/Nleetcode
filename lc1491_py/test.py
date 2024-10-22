import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().average(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        salary = [4000,3000,1000,2000]
        expected = 2500.00000
        self.t(salary, expected)
    
    def test2(self):
        salary = [1000,2000,3000]
        expected = 2000.00000
        self.t(salary, expected)


if __name__ == '__main__':
    unittest.main()
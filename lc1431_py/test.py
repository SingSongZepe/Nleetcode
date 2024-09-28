import unittest
from main import *

true = True
false = False

class Test(unittest.TestCase):
    def t(self, candies, extraCandies, expected=None):
        result = Solution().kidsWithCandies(candies, extraCandies)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected = [true,true,true,false,true]
        self.t(candies, extraCandies, expected)

    def test2(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected = [true,false,false,false,false]
        self.t(candies, extraCandies, expected)

if __name__ == '__main__':
    unittest.main()
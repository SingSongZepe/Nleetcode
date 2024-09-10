import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().insertGreatestCommonDivisors(arg)
        print_list(result)
        
    def test1(self):
        head = build_list([18, 6, 10, 3])
        self.t(head)

    def test2(self):
        head = build_list([7])
        self.t(head)


    def test_gcd(self):
        self.assertEqual(gcd(18, 6), 6)
        self.assertEqual(gcd(6, 10), 2)
        self.assertEqual(gcd(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
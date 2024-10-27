import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, l1, l2, expected=None):
        result = Solution().addTwoNumbers(l1, l2)
        print_list(result)

        while result and expected:
            if result.val != expected.val:
                raise Exception('different')
            result = result.next
            expected = expected.next
        
    def test1(self):
        l1 = build_list([7, 2, 4, 3])
        l2 = build_list([5, 6, 4])
        expected = build_list([7, 8, 0, 7])
        self.t(l1, l2, expected)

    def test2(self):
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        expected = build_list([8, 0, 7])
        self.t(l1, l2, expected)

    def test3(self):
        l1 = build_list([0])
        l2 = build_list([0])
        expected = build_list([0])
        self.t(l1, l2, expected)

    def test4(self):
        l1 = build_list([9, 4, 3])
        l2 = build_list([5, 6, 4])
        expected = build_list([1, 5, 0, 7])
        self.t(l1, l2, expected)

    def test5(self):
        l1 = build_list([1])
        l2 = build_list([9, 9])
        expected = build_list([1, 0, 0])
        self.t(l1, l2, expected)

    def test6(self):
        l1 = build_list([8, 9, 9])
        l2 = build_list([2])
        expected = build_list([9, 0, 1])
        self.t(l1, l2, expected)

if __name__ == '__main__':
    unittest.main()
import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().smallestRange(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().smallestRange(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        expected = [20,24]
        self.t(nums, expected)

    def test2(self):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected = [1, 1]
        self.t(nums, expected)

    def test3(self):
        nums = [[4, 10, 15], [5, 10, 11]]
        expected = [10, 10]
        self.t(nums, expected)

    def test4(self):
        nums = [[4, 9, 15], [6, 10, 10]]
        expected = [9, 10]
        self.t(nums, expected)

    def test5(self):
        nums = [[4, 9, 15], [6, 10]]
        expected = [9, 10]
        self.t(nums, expected)

    def test11(self):
        nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        expected = [20,24]
        self.t1(nums, expected)

    def test21(self):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected = [1, 1]
        self.t1(nums, expected)

    def test31(self):
        nums = [[4, 10, 15], [5, 10, 11]]
        expected = [10, 10]
        self.t1(nums, expected)


    def test_dual_heap(self):
        dh = DualHeap()
        dh.push(1)
        dh.push(2)
        dh.push(3)
        dh.push(3)

        a = dh.pop_min()
        print(a)

        b = dh.pop_max()
        print(b)

        c = dh.get_max()
        print(c)

        b = dh.pop_max()
        print(b)

        c = dh.get_max()
        print(c)


if __name__ == '__main__':
    unittest.main()
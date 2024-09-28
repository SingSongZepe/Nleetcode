import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        queue = MyCircularDeque(arg[0])

        # insert last
        res1 = queue.insertLast(arg[1])
        print(res1)
        self.assertEqual(res1, expected[0])

        # insert last
        res2 = queue.insertLast(arg[2])
        print(res2)
        self.assertEqual(res2, expected[1])

        # insert first
        res3 = queue.insertFront(arg[3])
        print(res3)
        self.assertEqual(res3, expected[2])

        # insert first
        res4 = queue.insertFront(arg[4])
        print(res4)
        self.assertEqual(res4, expected[3])

        # get last
        res5 = queue.getRear()
        print(res5)
        self.assertEqual(res5, expected[4])

        # is full
        res6 = queue.isFull()
        print(res6)
        self.assertEqual(res6, expected[5])

        # delete last
        res7 = queue.deleteLast()
        print(res7)
        self.assertEqual(res7, expected[6])

        # insert front
        res8 = queue.insertFront(arg[5])
        print(res8)
        self.assertEqual(res8, expected[7])

        # get front
        res9 = queue.getFront()
        print(res9)
        self.assertEqual(res9, expected[8])

        
    def test1(self):
        arg = [l[0] for l in [[3], [1], [2], [3], [4], [4]]]
        expected = [True, True, True, False, 2, True, True, True, 4]
        self.t(arg, expected)


if __name__ == '__main__':
    unittest.main()
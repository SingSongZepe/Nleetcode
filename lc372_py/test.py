import unittest
from main import *



def right_shift(b: List[int]) -> List[int]:
    for i in range(len(b) - 1, 0, -1):
        b[i] = b[i] // 2 + (5 if b[i - 1] % 2 == 1 else 0)
    b[0] = b[0] // 2
    return b


class Test(unittest.TestCase):
    def t(self, a, b, expected=None):
        result = Solution().superPow(a, b)
        print(result)
        self.assertEqual(result, expected)

    def t2(self, a, b, expected=None):
        result = Solution2().superPow(a, b)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        a = 2
        b = [3]
        expected = 8
        self.t(a, b, expected)

    def test2(self):
        a = 2
        b = [1, 0]
        expected = 1024
        self.t(a, b, expected)

    def test3(self):
        a = 1
        b = [4,3,3,8,5,2]
        expected = 1
        self.t(a, b, expected)

    def test12(self):
        a = 2
        b = [3]
        expected = 8
        self.t2(a, b, expected)

    def test22(self):
        a = 2
        b = [1, 0]
        expected = 1024
        self.t2(a, b, expected)

    def test32(self):
        a = 1
        b = [4,3,3,8,5,2]
        expected = 1
        self.t2(a, b, expected)


    def test42(self):
        a = 2
        b = [1, 0, 2, 4]
        expected = 457
        self.t2(a, b, expected)


    def test_right_shift(self):
        v = [1, 0]
        print(right_shift(v))
        v = [1, 2]
        print(right_shift(v))
        v = [1, 0, 2, 4]
        print(right_shift(v))
        v = [1, 0, 3, 5]
        print(right_shift(v))
        v = [3, 1, 4]
        print(right_shift(v))
        v = [9, 1, 2]
        print(right_shift(v))


if __name__ == '__main__':
    unittest.main()
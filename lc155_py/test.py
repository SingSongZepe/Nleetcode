import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, val, expected=None):
        # Your MinStack object will be instantiated and called as such:
        obj = MinStack()

        obj.push(val)
        obj.pop()

        param_3 = obj.top()
        print(param_3)

        param_4 = obj.getMin()
        print(param_4)

    def test1(self):
        val = 3
        expected = None
        self.t(val, expected)

if __name__ == '__main__':
    unittest.main()
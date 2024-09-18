import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, tasks, n, expected=None):
        result = Solution().leastInterval(tasks, n)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2
        expected = 8
        self.t(tasks, n, expected)

    def test2(self):
        tasks = ["A","C","A","B","D","B"]
        n = 1
        expected = 6
        self.t(tasks, n, expected)

    def test3(self):
        tasks = ["A","A","A", "B","B","B"]
        n = 3
        expected = 10
        self.t(tasks, n, expected)

if __name__ == '__main__':
    unittest.main()
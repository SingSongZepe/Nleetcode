import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution2().removeSubfolders(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        expected = ["/a","/c/d","/c/f"]
        self.t(folder, expected)

    def test2(self):
        folder = ["/a", "/a/b/c", "/a/b/d"]
        expected = ["/a"]
        self.t(folder, expected)

    def test3(self):
        folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        expected = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        self.t(folder, expected)

    def test4(self):
        folder = ['/leetcode', '/leetcode/problems']
        expected = ['/leetcode']
        self.t(folder, expected)

    def test5(self):
        folder = ["/ah/al/am","/ah/al"]
        expected = ['/ah/al']
        self.t(folder, expected)


if __name__ == '__main__':
    unittest.main()
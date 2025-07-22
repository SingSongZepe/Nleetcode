import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().deleteDuplicateFolder(arg)
        print(result)
    
    def t1(self, arg, expected=None):
        result = Solution1().deleteDuplicateFolder(arg)
        print(result)
        
    # def test1(self):
    #     paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
    #     expected = [["c"],["c","b"],["a"],["a","b"]]
    #     self.t(paths, expected)

    # def test2(self):
    #     paths = [["a","b"],["c","d"],["c"],["a"]]
    #     expected = [["c"],["c","d"],["a"],["a","b"]]
    #     self.t(paths, expected)

    # def test3(self):
    #     paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    #     expected = [["d"],["d","a"]]
    #     self.t(paths, expected)
    
    def test11(self):
        paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
        expected = [["c"],["c","b"],["a"],["a","b"]]
        self.t1(paths, expected)

    def test21(self):
        paths = [["a","b"],["c","d"],["c"],["a"]]
        expected = [["c"],["c","d"],["a"],["a","b"]]
        self.t1(paths, expected)

    def test31(self):
        paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
        expected = [["d"],["d","a"]]
        self.t1(paths, expected)


if __name__ == '__main__':
    unittest.main()
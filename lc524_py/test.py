import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, dictionary, expected=None):
        result = Solution().findLongestWord(s, dictionary)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, s, dictionary, expected=None):
        result = Solution().findLongestWord(s, dictionary)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        s = 'abpcplea'
        dictionary = ['ale', 'apple', 'monkey', 'plea']
        expected = 'apple'
        self.t(s, dictionary, expected)

    def test2(self):
        s = 'abpcplea'
        dictionary = ['a', 'b', 'c']
        expected = 'a'
        self.t(s, dictionary, expected)

    def test3(self):
        s = "abpcplea"
        dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
        expected = "apple"
        self.t(s, dictionary, expected)

    def test4(self):
        s = "apple"
        dictionary = ["zxc","vbn"]
        expected = ''
        self.t(s, dictionary, expected)


    def test11(self):
        s = 'abpcplea'
        dictionary = ['ale', 'apple', 'monkey', 'plea']
        expected = 'apple'
        self.t1(s, dictionary, expected)

    def test21(self):
        s = 'abpcplea'
        dictionary = ['a', 'b', 'c']
        expected = 'a'
        self.t1(s, dictionary, expected)

    def test31(self):
        s = "abpcplea"
        dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
        expected = "apple"
        self.t1(s, dictionary, expected)

    def test41(self):
        s = "apple"
        dictionary = ["zxc","vbn"]
        expected = ''
        self.t1(s, dictionary, expected)


if __name__ == '__main__':
    unittest.main()
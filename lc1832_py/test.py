import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().checkIfPangram(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        sentence = "thequickbrownfoxjumpsoverthelazydog"
        expected = True
        self.t(sentence, expected)

    def test2(self):
        sentence = "leetcode"
        expected = False
        self.t(sentence, expected)

if __name__ == '__main__':
    unittest.main()
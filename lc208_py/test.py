import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, word, prefix, expected=None):
        obj = Trie()
        obj.insert(word)
        param_2 = obj.search(word)
        param_3 = obj.search(prefix)
        param_4 = obj.startsWith(prefix)
        obj.insert(word)
        param_5 = obj.search(word)

        self.assertEqual(param_2, True)
        self.assertEqual(param_3, False)
        self.assertEqual(param_4, True)
        self.assertEqual(param_5, True)

    def t1(self, word, prefix, expected=None):
        obj = Trie1()
        obj.insert(word)
        param_2 = obj.search(word)
        param_3 = obj.search(prefix)
        param_4 = obj.startsWith(prefix)
        obj.insert(word)
        param_5 = obj.search(word)

        self.assertEqual(param_2, True)
        self.assertEqual(param_3, False)
        self.assertEqual(param_4, True)
        self.assertEqual(param_5, True)

    def test1(self):
        word = 'apple'
        prefix = 'app'
        self.t(word, prefix)

    def test11(self):
        word = 'apple'
        prefix = 'app'
        self.t1(word, prefix)


if __name__ == '__main__':
    unittest.main()
import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, words, k, expected=None):
        result = Solution().topKFrequent(words, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        expected = ["i", "love"]
        self.t(words, k, expected)

    def test2(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        expected = ["the","is","sunny","day"]
        self.t(words, k, expected)

    def test3(self):
        words = ["i","love","leetcode","i","love","coding"]
        k = 3
        expected = ["i","love","coding"]
        self.t(words, k, expected)

if __name__ == '__main__':
    unittest.main()
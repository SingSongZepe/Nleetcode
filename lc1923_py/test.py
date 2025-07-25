import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestCommonSubpath(*arg)
        self.assertEqual(result, expected)
        print(result)
        
    def test1(self):
        n = 5
        paths = [[0,1,2,3,4],
               [2,3,4],
               [4,0,1,2,3]]
        expected = 2
        self.t([n, paths], expected)

    def test2(self):
        n = 3
        paths = [[0], [1], [2]]
        expected = 0
        self.t([n, paths], expected)

    def test3(self):
        n = 5
        paths = [[0,1,0,1,0,1,0,1,0],
                 [0,1,3,0,1,4,0,1,0]]
        expected = 3
        self.t([n, paths], expected)

    def test_hash_method(self):

        base = 10007
        mod = 2**63 - 1  # A large prime number for modding to avoid collisions

        def get_hashes(path, length):
            h = 0
            hashes = set()
            base_l = pow(base, length, mod)

            for i in range(length):
                h = (h * base + path[i]) % mod

            hashes.add(h)
            for i in range(length, len(path)):
                h = (h * base - path[i - length] * base_l + path[i]) % mod
                hashes.add(h)
            return hashes

if __name__ == '__main__':
    unittest.main()
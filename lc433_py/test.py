import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, sg, eg, bank, expected=None):
        result = Solution().minMutation(sg, eg, bank)
        print(result)

    def t2(self, sg, eg, bank, expected=None):
        result = Solution2().minMutation(sg, eg, bank)
        print(result)

    def test1(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        self.t(startGene, endGene, bank, expected)

    def test2(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        self.t(startGene, endGene, bank, expected)


    def test21(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        self.t2(startGene, endGene, bank, expected)

    def test22(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        self.t2(startGene, endGene, bank, expected)

if __name__ == '__main__':
    unittest.main()
import unittest
from main import *

null = None

class Test(unittest.TestCase):
    def t(self, arg, ops, expected=None):
        allone = AllOne()

        for (i, a), op in zip(enumerate(arg), ops):
            match op:
                case 'inc':
                    allone.inc(a[0])
                case 'dec':
                    allone.dec(a[0])
                case 'getMaxKey':
                    actual = allone.getMaxKey()
                    print(actual)
                    self.assertEqual(actual, expected[i])
                case 'getMinKey':
                    actual = allone.getMinKey()
                    print(actual)
                    self.assertEqual(actual, expected[i])



        
    def test1(self):
        ops = ['inc', 'inc', 'getMaxKey', "getMinKey", "inc", "getMaxKey", "getMinKey" ]
        arg = [['hello'], ['hello'], [], [], ['leet'], [], []]
        expected = [null, null, 'hello', 'hello', null,  'hello', 'leet']
        self.t(arg, ops, expected)

    def test2(self):
        ops = ["inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
        arg = [["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
        expected = [null,null,null,null,null,null,null,null,"a",null,"c","c"]
        self.t(arg, ops, expected)

if __name__ == '__main__':
    unittest.main()
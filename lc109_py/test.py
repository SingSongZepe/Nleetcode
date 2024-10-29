import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sortedListToBST(arg)
        print(result)
        self.assertEqual(inorder(result), collect_linked_list(arg))
        
    def test1(self):
        head = build_linked_list([-10, -3, 0, 5, 9])
        print_linked_list(head)
        self.t(head)


if __name__ == '__main__':
    unittest.main()
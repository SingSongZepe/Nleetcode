import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().hasCycle(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        head = build_list([3, 2, 0, -4])
        pos = 1

        curr, prev = head, head
        while curr.next:
            if pos == 0:
                prev = curr
            curr = curr.next
            pos -= 1
        tail = curr
        tail.next = prev

        self.t(head, True)

    def test2(self):
        head = build_list([1, 2])
        pos = 0

        curr, prev = head, head
        while curr.next:
            if pos == 0:
                prev = curr
            curr = curr.next
            pos -= 1
        tail = curr
        tail.next = prev

        self.t(head, True)


    def test3(self):
        head = build_list([1])
        pos = -1

        curr, prev = head, None
        while curr.next:
            if pos == 0:
                prev = curr
            curr = curr.next
            pos -= 1
        tail = curr
        tail.next = prev

        self.t(head, False)

if __name__ == '__main__':
    unittest.main()
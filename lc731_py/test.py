import unittest
from main import *

true = True
false = False


class Test(unittest.TestCase):
    def t(self, books, expected=None):
        calendar = MyCalendarTwo()
        for i, book in enumerate(books):
            res = calendar.book(book[0], book[1])
            print(res)
            self.assertEqual(res, expected[i])


    def test1(self):
        books = [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]
        expected = [true, true, true, false, true, true]
        self.t(books, expected)

if __name__ == '__main__':
    unittest.main()
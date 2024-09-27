import unittest
from main import *


true = True
false = False

class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        calender = MyCalendar()
        for i in range(len(arg)):
            res = calender.book(arg[i][0], arg[i][1])
            print(arg[i], res)
            self.assertEqual(res, expected[i])

    def t1(self, arg, expected=None):
        calender = MyCalendar1()
        for i in range(len(arg)):
            res = calender.book(arg[i][0], arg[i][1])
            print(arg[i], res)
            self.assertEqual(res, expected[i])
        
    def test1(self):
        arg = [[10, 20], [15, 25], [20, 30]]
        expected = [True, False, True]
        self.t(arg, expected)

    def test2(self):
        arg = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
        expected = [true,true,false,false,true,false,true,true,true,false]
        self.t(arg, expected)

    def test11(self):
        arg = [[10, 20], [15, 25], [20, 30]]
        expected = [True, False, True]
        self.t1(arg, expected)

    def test21(self):
        arg = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
        expected = [true,true,false,false,true,false,true,true,true,false]
        self.t1(arg, expected)


if __name__ == '__main__':
    unittest.main()
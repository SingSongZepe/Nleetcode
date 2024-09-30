import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        custom_stack = CustomStack(arg[0])
        # for (i, op), a in zip(enumerate(ops), arg[1:]):
        #     match op:
        #         case "push":
        #             custom_stack.push(a)
        #             print(custom_stack.stack)
        #         case "pop":
        #             res = custom_stack.pop()
        #             print(custom_stack.stack)
        #             self.assertEqual(res, expected[i])
        #         case "increment":
        #             custom_stack.increment(i, a)
        #             print(custom_stack.stack)

        custom_stack.push(0)
        custom_stack.push(1)
        custom_stack.push(2)
        custom_stack.push(3)

        custom_stack.increment(arg[0][0], arg[0][1])
        print(custom_stack.stack)



    def test1(self):
        arg = [[5, 10]]
        self.t(arg)



if __name__ == '__main__':
    unittest.main()
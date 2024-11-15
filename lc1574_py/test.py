import unittest
from main import *


class Test(unittest.TestCase):
    def test1(self):
        arr = [1,2,3,10,4,2,3,5]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 3)

    def test2(self):
        arr = [5, 4, 3, 2, 1]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 4)

    def test3(self):
        arr = [1, 2, 3]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 0)

    def test4(self):
        arr = [1, 2, 1]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 1)

    def test5(self):
        arr = [2,2,2,1,1,1]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 3)

    def test6(self):
        arr = [6,3,10,11,15,20,13,3,18,12]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 8)

    def test7(self):
        arr = [16,10,0,3,22,1,14,7,1,12,15]
        result = Solution().findLengthOfShortestSubarray(arr)
        print(result)
        self.assertEqual(result, 8)


    # def test11(self):
    #     arr = [1,2,3,10,4,2,3,5]
    #     result = Solution1().findLengthOfShortestSubarray(arr)
    #     print(result)
    #
    # def test21(self):
    #     arr = [5, 4, 3, 2, 1]
    #     result = Solution1().findLengthOfShortestSubarray(arr)
    #     print(result)
    #
    # def test31(self):
    #     arr = [1, 2, 3]
    #     result = Solution1().findLengthOfShortestSubarray(arr)
    #     print(result)



if __name__ == '__main__':
    unittest.main()
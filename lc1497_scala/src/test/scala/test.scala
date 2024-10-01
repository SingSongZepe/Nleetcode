
import scala.Solution

object test {
  def t(arr: Array[Int], k: Int, expected: Option[Boolean] = None): Unit = {
    val res = Solution.canArrange(arr,k)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {
    val arr = Array(1, 2, 3, 4, 5, 10, 6, 7, 8, 9)
    val k = 5
    val expected = Some(true)
    t(arr, k, expected)
  }
  def test2(): Unit = {
    val arr = Array(1, 2, 3, 4, 5, 6)
    val k = 7
    val expected = Some(true)
    t(arr, k, expected)
  }
  def test3(): Unit = {
    val arr = Array(1, 2, 3, 4, 5, 6)
    val k = 10
    val expected = Some(false)
    t(arr, k, expected)
  }
  def test4(): Unit = {
    val arr = Array(10, -10)
    val k = 2
    val expected = Some(true)
    t(arr, k, expected)
  }

  def main(array: Array[String]): Unit = {
    test1()
    test2()
    test3()
    test4()
  }
}

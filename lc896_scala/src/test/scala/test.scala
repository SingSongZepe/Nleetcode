
//import scala.Solution

object test {
  def t(arg: Array[Int], expected: Option[Boolean] = None): Unit = {
    val res = Solution.isMonotonic(arg)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {
    val nums = Array(1, 2, 2, 3)
    val expected = Some(true)
    test.t(nums, expected)
  }
  def test2(): Unit = {
    val nums = Array(1, 1, 0)
    val expected = Some(true)
    test.t(nums, expected)
  }
  def test3(): Unit = {
    val nums = Array(1, 1, 2)
    val expected = Some(true)
    test.t(nums, expected)
  }

  def main(array: Array[String]): Unit = {
    test1()
    test2()
    test3()
  }
}

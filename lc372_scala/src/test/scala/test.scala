
import scala.Solution

object test {
  def t(a: Int, b: Array[Int], expected: Option[Int] = None): Unit = {
    val res = Solution.superPow(a, b)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {
    val a = 2
    val b = Array(3)
    val expected = Some(8)
    t(a, b, expected)
  }
  def test2(): Unit = {
    val a = 2
    val b = Array(1, 0)
    val expected = Some(1024)
    t(a, b, expected)
  }
  def test3(): Unit = {
    val a = 1
    val b = Array(4, 3, 3, 8, 5, 2)
    val expected = Some(1)
    t(a, b, expected)
  }
  def test4(): Unit = {
    val a = 2
    val b = Array(1, 0, 2, 4)
    val expected = Some(457)
    t(a, b, expected)
  }



  def main(array: Array[String]): Unit = {
    test1()
    test2()
    test3()
    test4()
  }
}

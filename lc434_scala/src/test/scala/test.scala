
import scala.Solution

object test {
  def t(arg: String, expected: Option[Int] = None): Unit = {
    val res = Solution.countSegments(arg)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {
    val s = "Hello, my name is John"
    val expected = Some(5)
    t(s, expected)
  }
  def test2(): Unit = {
    val s = "Hello"
    val expected = Some(1)
    t(s, expected)
  }
  def test3(): Unit = {
    val s = ""
    val expected = Some(0)
    t(s, expected)
  }
  def test4(): Unit = {
    val s = "                "
    val expected = Some(0)
    t(s, expected)
  }




  def main(array: Array[String]): Unit = {
    test1()
    test2()
    test3()
    test4()
  }
}

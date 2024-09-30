
import scala.Solution

object test {
  def t(arg: String, expected: Option[String] = None): Unit = {
    var res = Solution.solve(arg)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {

  }
  def test2(): Unit = {

  }



  def main(array: Array[String]): Unit = {
    test1()
    test2()
  }
}


import scala.Solution
import scala.Builder

object test {
  def t(arg: String, expected: Option[String] = None): Unit = {
//    var res = Solution.increasingBST(arg)
//    if (expected.isDefined) {
//      assert(res == expected.get)
//    } else {
//      println("expected not equals to result")
//    }
  }

  def test1(): Unit = {

  }
  def test2(): Unit = {

  }

  def test_build_tree1(): Unit = {
    val root: TreeNode = Builder.build_tree(Array(5, 1, 7))
    println(s"root value: ${root.value}")
  }
  def test_build_tree2(): Unit = {
    val root: TreeNode = Builder.build_tree(Array(5, 1, -1, -1, 7))
    println(s"root value: ${root.value}")
  }



  def main(array: Array[String]): Unit = {
    test1()
    test2()

    // test build
    test_build_tree1()
    test_build_tree2()
  }
}

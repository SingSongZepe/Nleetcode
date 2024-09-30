
import scala.CustomStack

object test {
  def t(arg: Array[Int], expected: Option[String] = None): Unit = {
    println("Hello World!")
  }

  def test1(): Unit = {
    var stk = new CustomStack(3)
    // push 1
    stk.push(1)
    // push 2
    stk.push(2)
    // pop == 2
    val pop1 = stk.pop()
    assert(pop1 == 2)
    // push 2
    stk.push(2)
    // push 3
    stk.push(3)
    // push 4
    stk.push(4)
    // increment [5, 100]
    stk.increment(5, 100)
    // increment [2, 100]
    stk.increment(2, 100)
    // pop == 103
    val pop2 = stk.pop()
    assert(pop2 == 103)
    // pop == 202
    val pop3 = stk.pop()
    assert(pop3 == 202)
    // pop == 201
    val pop4 = stk.pop()
    assert(pop4 == 201)
    // pop == -1
    val pop5 = stk.pop()
    assert(pop5 == -1)
  }
  def test2(): Unit = {

  }



  def main(array: Array[String]): Unit = {
    test1()
    test2()
  }
}


package scala


object Solution {
  def superPow(_a: Int, b: Array[Int]): Int = {
    if (_a == 1) return 1

    val a = _a % 1337
    var temp = a * a
    var circle_length = 1
    while (temp != a) {
      temp = (temp * a) % 1337
      circle_length += 1
    }

    var tot = 0
    for (n <- b) {
      tot = (tot * 10 + n) % circle_length
    }

    if (tot == 0) return a

    var res = 1
    for (_ <- 0 until tot) {
      res = (res * a) % 1337
    }
    res
  }
}


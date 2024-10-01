
package scala

import scala.collection.mutable

object Solution {
  def canArrange(arr: Array[Int], k: Int): Boolean = {
    val cnter = mutable.HashMap[Int, Int]()

    for (_a <- arr) {
      val a = ((_a % k) + k) % k
      cnter.update(a, cnter.getOrElse(a, 0) + 1)
    }

    var canArranged = true
    for (i <- 0 until k / 2) {
      val v = cnter.getOrElse(i, 0)
      if (v != 0) {
        if (i == 0) {
          canArranged = v % 2 == 0
        } else {
          canArranged = v == cnter.getOrElse(k-i, -1)
        }
      }
    }
    canArranged

  }
}
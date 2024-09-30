
package scala

object Solution {
  def isMonotonic(nums: Array[Int]): Boolean = {
    if (nums.length <= 1) true
    else {
      val isIncreasing = nums(0) < nums.last
      var monotone = true
      for (i <- 1 until nums.length) {
        if (isIncreasing && nums(i) < nums(i - 1)) {
          monotone = false
        } else if (!isIncreasing && nums(i) > nums(i - 1)) {
          monotone = false
        }
      }
      monotone
    }
  }
}
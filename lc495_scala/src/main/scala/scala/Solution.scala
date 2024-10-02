
package scala


object Solution {
  def findPoisonedDuration(timeSeries: Array[Int], duration: Int): Int = {

    var cnt = 0
    for (i <- 0 until timeSeries.length - 1) {
      cnt += math.min(duration, timeSeries(i + 1) - timeSeries(i))
    }
    cnt + duration
  }
}
package scala

object Solution1 {
  def findPoisonedDuration(timeSeries: Array[Int], duration: Int): Int = {
    timeSeries
      .zip(timeSeries.tail)
      .map { case (current, next) =>
        math.min(duration, next - current)
      }
      .sum + duration
  }
}

package scala

object NewFeature {
  def test1(timeSeries: Array[Int]): Unit = {
    val a = timeSeries
      .zip(timeSeries.tail)
    println("test1")
  }
}

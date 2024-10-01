package scala

// in scala 2.13
// the mapValues function has been discarded

object Solution1 {
  def canArrange(arr: Array[Int], k: Int): Boolean = {
    lazy val cnter = arr.toList.map { n => ((n % k) + k) % k }
      .groupBy(identity)
      .mapValues(_.size)
//      .toMap

    cnter.forall{case (k1,v1) =>
      if(k1 == 0) (v1 % 2) == 0
      else cnter.get(k-k1).map(_ == v1).getOrElse(false)
    }
  }
}
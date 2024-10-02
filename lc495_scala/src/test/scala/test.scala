

object test {
  def t(ts: Array[Int], duration: Int, expected: Option[Int] = None): Unit = {
    val res = Solution.findPoisonedDuration(ts, duration)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def t1(ts: Array[Int], duration: Int, expected: Option[Int] = None): Unit = {
    val res = Solution1.findPoisonedDuration(ts, duration)
    if (expected.isDefined) {
      assert(res == expected.get)
    } else {
      println("expected not equals to result")
    }
  }

  def test1(): Unit = {
    val ts = Array(1, 4)
    val duration = 2
    val expected = Some(4)
    t(ts, duration, expected)
  }
  def test2(): Unit = {
    val ts = Array(1, 2)
    val duration = 2
    val expected = Some(3)
    t(ts, duration, expected)
  }

  def test11(): Unit = {
    val ts = Array(1, 4)
    val duration = 2
    val expected = Some(4)
    t1(ts, duration, expected)
  }
  def test21(): Unit = {
    val ts = Array(1, 2)
    val duration = 2
    val expected = Some(3)
    t1(ts, duration, expected)
  }


  def test_new_feature_test1(): Unit = {
    val ts = Array(1, 2, 3, 4, 5)
    NewFeature.test1(ts)
  }

  def main(array: Array[String]): Unit = {
//    test1()
//    test2()
//    test11()
//    test21()
    test_new_feature_test1()
  }
}

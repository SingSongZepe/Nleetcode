
package scala

class CustomStack(_maxSize: Int) {
  val _msize: Int = _maxSize
  var stack: Array[Int] = new Array(_maxSize)
  var tail: Int = 0

  def push(x: Int): Unit = {
    if (tail < _msize) {
      stack(tail) = x
      tail += 1
    }
  }

  def pop(): Int = {
    if (tail > 0) {
      tail -= 1
      stack(tail)
    } else {
      -1
    }
  }

  def increment(k: Int, `val`: Int): Unit = {
    for (i <- 0 until math.min(k, tail)) {
      stack(i) += `val`
    }
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * val obj = new CustomStack(maxSize)
 * obj.push(x)
 * val param_2 = obj.pop()
 * obj.increment(k,`val`)
 */
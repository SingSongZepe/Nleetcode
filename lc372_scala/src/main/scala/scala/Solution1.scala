
package scala


object Solution1 {
  def superPow(a: Int, b: Array[Int]): Int = superPow(a, b, b.length-1)

  def superPow(a: Int, b: Array[Int], index: Int): Int =
    if (index == 0)pow(a, b(index)) % 1337
    else (pow(superPow(a, b, index-1), 10) * pow(a, b(index))) % 1337

  def pow(x: Int, n: Int): Int =
    if (n == 0) 1
    else if (n == 1) x % 1337
    else {
      val half = pow(x, n/2)
      if (n % 2 == 0) (half * half) % 1337
      else (((half * half) % 1337) * (x % 1337)) % 1337
    }
}
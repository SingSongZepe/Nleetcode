
package scala


object Solution {
  def countSegments(s: String): Int = {
    if (s.isEmpty) 0
    else s.split("\\s+").count(_.nonEmpty)
  }
}
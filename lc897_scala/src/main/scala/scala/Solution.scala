
package scala

import scala.annotation.tailrec


class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def increasingBST(root: TreeNode): TreeNode = {
    val values = scala.collection.mutable.ListBuffer[Int]()

    def inorderTraversal(node: TreeNode): Unit = {
      if (node != null) {
        inorderTraversal(node.left)
        values += node.value
        inorderTraversal(node.right)
      }
    }

    inorderTraversal(root)

    if (values.isEmpty) return null

    val newRoot = new TreeNode(values.head)
    var current = newRoot
    for (value <- values.tail) {
      current.right = new TreeNode(value)
      current = current.right
    }

    newRoot
  }
}


object Builder {
  def build_tree(arr: Array[Int]): TreeNode = {
    def build(i: Int): TreeNode = {
      if (i < arr.length && arr(i) != -1) { // -1 represents a Null Node
        val node = new TreeNode(arr(i))
        node.left = build(2*i + 1)
        node.right = build(2*i + 2)
        return node
      }
      null
    }
    build(0)
  }
}

object Printer {
  @tailrec
  def print_right(_root: TreeNode): Unit = {
    if (_root == null) {
      return
    }
    print(s"${_root.value} -> ")
    print_right(_root.right)
  }
}

//object Printer {
//  def print_right(_arr: TreeNode): Unit = {
//    var arr: TreeNode = _arr
//    while (arr != null) {
//      print(s"${arr.value} -> ")
//      arr = arr.right
//    }
//  }
//}
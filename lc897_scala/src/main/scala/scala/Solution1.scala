package scala


// better solution
object Solution1 {
  def increasingBST(root: TreeNode): TreeNode = {
    val dummyHead = new TreeNode()
    def travel(root: TreeNode, _cur: TreeNode): Option[TreeNode] = {
      if (root == null) Some(_cur)
      else {
        val cur = travel(root.left, _cur).getOrElse(_cur)
        cur.right = new TreeNode(root.value)
        travel(root.right, cur.right)
      }
    }
    travel(root, dummyHead)
    dummyHead.right
  }
}
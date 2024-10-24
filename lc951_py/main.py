
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val != root2.val:
            return False

        def match(root1: TreeNode, root2: TreeNode) -> bool:
            l1 = root1.left
            r1 = root1.right
            l2 = root2.left
            r2 = root2.right

            if not (l1 or l2 or r1 or r2):
                return True
            elif l1 and r1 and l2 and r2:
                if l1.val == l2.val and r1.val == r2.val:
                    return match(l1, l2) and match(r1, r2)
                elif l1.val == r2.val and r1.val == l2.val:
                    return match(l1, r2) and match(r1, l2)
            elif l1 and l2 and not (r1 or r2):
                if l1.val == l2.val:
                    return match(l1, l2)
            elif l1 and r2 and not (r1 or l2):
                if l1.val == r2.val:
                    return match(l1, r2)
            elif r1 and l2 and not (l1 or r2):
                if r1.val == l2.val:
                    return match(r1, l2)
            elif r1 and r2 and not (l1 or l2):
                if r1.val == r2.val:
                    return match(r1, r2)

            return False

        return match(root1, root2)


class Solution1:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val != root2.val:
            return False

        l = self.flipEquiv(root1.left, root2.left)
        if l:
            r = self.flipEquiv(root1.right, root2.right)
        else:
            l = self.flipEquiv(root1.right, root2.left)
            if l:
                r = self.flipEquiv(root1.left, root2.right)
            else:
                return False


        return l and r

# a simplified solution
# dividing into two parts to compare
# if sub-left is a flip equivalent tree
# then check whether the sub-right is or not
# if sub-left is not
# then compare sub-left1 with sub-right2
# and sub-right1 with sub-left2
class Solution2:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        left_res = self.flipEquiv(root1.left, root2.left)
        if left_res:
            right_res = self.flipEquiv(root1.right, root2.right)
        else:
            left_res = self.flipEquiv(root1.left, root2.right)
            if left_res:
                right_res = self.flipEquiv(root1.right, root2.left)
            else:
                return False
        return left_res and right_res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
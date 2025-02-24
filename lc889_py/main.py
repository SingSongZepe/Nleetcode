
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        node = TreeNode(preorder[0])
        n = len(preorder)
        for i in range(1, n):
            if set(preorder[1:i+1]) == set(postorder[:i]):
                node.left = self.constructFromPrePost(preorder[1:i+1], postorder[0:i])
                node.right = self.constructFromPrePost(preorder[i+1:], postorder[i:-1])
                break

        return node


# better solution
class Solution1:
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

def main():
    print('Hello World')

if __name__ == '__main__':
    main()



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        ref: TreeNode = None

        def dfs(n1: TreeNode, n2: TreeNode) -> TreeNode | None:
            nonlocal ref
            if ref:
                return

            if n1 == target:
                ref = n2
                return

            if n1.left:
                dfs(n1.left, n2.left)

            if n1.right:
                dfs(n1.right, n2.right)

        dfs(original, cloned)
        return ref




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
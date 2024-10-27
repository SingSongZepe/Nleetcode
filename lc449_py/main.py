
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # preorder
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def _preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            res.append(str(node.val))
            _preorder(node.left)
            _preorder(node.right)

        _preorder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        data = [int(n) for n in data.split(' ')]

        def _depreorder(data: List[int]) -> Optional[TreeNode]:
            if not data:
                return None
            elif len(data) == 1:
                return TreeNode(data[0])

            root = TreeNode(data[0])

            p, n = 1, len(data)
            while p < n and data[p] < data[0]:
                p += 1

            root.left = _depreorder(data[1:p])
            root.right = _depreorder(data[p:])

            return root

        return _depreorder(data)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
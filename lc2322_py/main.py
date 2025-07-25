
from typing import List

# failed method
# class TreeNode:
#     val: int
#     idx: int
#     children: List['TreeNode']
#     def __init__(self, idx: int, val: int):
#         self.idx = idx
#         self.val = val
#         self.children = []
#
# class Solution:
#     def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
#
#         # always take node 0 as root
#         edges.sort(key=lambda x: min(x[0], x[1]))
#
#         nodes = [TreeNode(idx, val) for idx, val in enumerate(nums)]
#         for p, c in edges:
#             nodes[p].children.append(nodes[c])
#             nodes[c].children.append(nodes[p])
#
#         subtree_xor = [0] * len(nums)
#         entry = [0] * len(nums)
#         exit_ = [0] * len(nums)
#
#         curr_time = 0
#         visited = [False] * len(nums)
#
#         def dfs(node: TreeNode) -> int:
#             visited[node.idx] = True
#
#             nonlocal curr_time
#             curr_time += 1
#             entry[node.idx] = curr_time
#
#             if not node.children:
#                 subtree_xor[node.idx] = node.val
#                 exit_[node.idx] = curr_time
#                 return node.val
#
#             xor = node.val
#             for child in node.children:
#                 if visited[child.idx]:
#                     continue
#                 xor ^= dfs(child)
#             subtree_xor[node.idx] = xor
#
#             exit_[node.idx] = curr_time
#
#             return xor
#
#         # always pass ent1 <= ent2 to this function
#         def is_subtree(idx1: int, idx2: int) -> bool:
#             return exit_[idx1] >= exit_[idx2] and entry[idx1] < entry[idx2]
#
#         dfs(nodes[0])
#
#         min_xor = float('inf')
#         for i in range(len(edges)-1):
#
#             # B A
#             p1, c1 = edges[i]
#             if is_subtree(c1, p1):
#                 p1, c1 = c1, p1
#
#             for j in range(i+1, len(edges)):
#                 xor_a = subtree_xor[c1]
#                 xor_b = subtree_xor[0] ^ xor_a
#
#                 p2, c2 = edges[j]
#                 if is_subtree(c2, p2):
#                     p2, c2 = c2, p2
#
#                 xor_c = subtree_xor[c2]
#                 if is_subtree(c1, c2):  # in subtree A
#                     xor_a = xor_a ^ xor_c
#                 else:
#                     xor_b = xor_b ^ xor_c
#
#                 min_xor = min(min_xor, max(xor_a, xor_b, xor_c) - min(xor_a, xor_b, xor_c))
#
#         return min_xor

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:

        n = len(nums)

        entry = [0] * n
        exit_ = [0] * n
        sub_xor = [0] * n
        min_xor = float('inf')

        adj = [[] for _ in range(n)]

        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)

        curr_time = 0
        def dfs(node: int, parent: int):
            nonlocal curr_time
            entry[node] = curr_time
            curr_time += 1

            xor = nums[node]
            for child in adj[node]:
                if child == parent:
                    continue
                dfs(child, node)
                xor ^= sub_xor[child]

            sub_xor[node] = xor

            exit_[node] = curr_time - 1

        # def dfs_1(node: int, parent: int, cnt: int) -> int:
        #
        #     # if no child
        #     if len(adj[node]) == 1 and adj[node][0] == parent:
        #         entry[node] = cnt
        #         exit_[node] = cnt
        #         sub_xor[node] = nums[node]
        #         return 1
        #
        #     entry[node] = cnt
        #     xor = nums[node]
        #     cnt_subtree = 1
        #     for child in adj[node]:
        #         if child == parent:
        #             continue
        #         cnt_subtree += dfs_1(child, node, cnt + cnt_subtree)
        #         xor ^= sub_xor[child]
        #
        #     sub_xor[node] = xor
        #
        #     exit_[node] = cnt + cnt_subtree
        #     return cnt_subtree

        dfs(0, -1)
        print('method 1')
        print(entry)
        print(exit_)
        print(sub_xor)

        # dfs_1(0, -1, 0)
        # print('method 2')
        # print(entry)
        # print(exit_)
        # print(sub_xor)

        # parent = [0] * n
        # stack = [(0, -1, False)]
        # while stack:
        #     node, p, visited = stack.pop()
        #     if not visited:
        #         parent[node] = p
        #         entry[node] = curr_time
        #         curr_time += 1
        #         stack.append((node, p, True))
        #         for neighbor in reversed(adj[node]):
        #             if neighbor != p:
        #                 stack.append((neighbor, node, False))
        #     else:
        #         sub_xor[node] = nums[node]
        #         for neighbor in adj[node]:
        #             if neighbor != p:
        #                 sub_xor[node] ^= sub_xor[neighbor]
        #         exit_[node] = curr_time - 1

        # if y is a node of x subtree
        # def is_subtree(x: int, y: int) -> bool:
        #     return entry[x] < entry[y] <= exit_[x]

        # select two nodes
        for x in range(1, n - 1):
            for y in range(x + 1, n):
                if entry[x] < entry[y] <= exit_[x]:
                    a = sub_xor[y]
                    b = sub_xor[x] ^ sub_xor[y]
                    c = sub_xor[0] ^ sub_xor[x]
                elif entry[y] < entry[x] <= exit_[y]:
                    a = sub_xor[x]
                    b = sub_xor[y] ^ sub_xor[x]
                    c = sub_xor[0] ^ sub_xor[y]
                else:
                    a = sub_xor[x]
                    b = sub_xor[y]
                    c = sub_xor[0] ^ sub_xor[x] ^ sub_xor[y]

                min_xor = min(min_xor, max(a, b, c) - min(a, b, c))

        return min_xor

# code snippet on how to use bfs to mark entry and exit time
#
# stack = [(0, -1, False)]
# while stack:
#     node, p, visited = stack.pop()
#     if not visited:
#         parent[node] = p
#         in_time[node] = time
#         time += 1
#         stack.append((node, p, True))
#         for neighbor in reversed(adj[node]):
#             if neighbor != p:
#                 stack.append((neighbor, node, False))
#     else:
#         xor[node] = nums[node]
#         for neighbor in adj[node]:
#             if neighbor != p:
#                 xor[node] ^= xor[neighbor]
#         out_time[node] = time - 1




def main():

    curr_time = 0

    def test():
        global curr_time

        print(curr_time)

    test()

    print('Hello World')

if __name__ == '__main__':
    main()







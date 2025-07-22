from typing import List, Dict

# failed solution
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        has = set()
        del_ = set()
        token = []
        def post_dfs(d: Dict) -> str:
            if len(d) == 0:
                token.clear()
                return ''
            for dir_ in d:
                d[dir_]['#'] = ''
                post_dfs(d[dir_])
                sig = '.'.join(token)
                d[dir_]['#'] += sig

                if d[dir_]['#'] in has:
                    del_.add(d[dir_]['#'])
                else:
                    has.add(d[dir_]['#'])
                token.append(dir_)

        result = []
        curr = []
        def dfs(d: Dict) -> None:
            for dir_ in d:
                if dir_ == '#':
                    continue
                if d[dir_]['#'] in del_:
                    continue
                curr.append(dir_)
                result.append(curr.copy())
                dfs(d[dir_])
                curr.pop()
        
        d = {}
        for path in paths:
            td = d
            for dir_ in path:
                if dir_ not in td:
                    td[dir_] = {}
                td = td[dir_]

        post_dfs(d)
        del_.remove('')
        dfs(d)

        return result


from collections import Counter

class Trie:
    # current node structure's serialized representation
    serial: str = ""
    # current node's child nodes
    children: dict

    def __init__(self):
        self.children = dict()

# ! nice solution
class Solution1:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # root node
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        # hash table records the occurrence times of each serialized representation
        freq = Counter()

        # post-order traversal based on depth-first search, calculate the serialized representation of each node structure
        def construct(node: Trie) -> None:
            # if it is a leaf node, then the serialization is represented as an empty string, and no operation is required.
            if not node.children:
                return

            v = list()
            # if it is not a leaf node, the serialization representation of the child node structure needs to be calculated first.
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")

            # to prevent issues with order, sorting is needed
            v.sort()
            node.serial = "".join(v)
            # add to hash table
            freq[node.serial] += 1

        construct(root)

        ans = list()
        # record the path from the root node to the current node.
        path = list()

        def operate(node: Trie) -> None:
            # if the serialization appears more than once in the hash table, it needs to be deleted.
            if freq[node.serial] > 1:
                return
            # otherwise add the path to the answer
            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
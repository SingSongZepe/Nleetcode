

from typing import List, Dict

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        trie = {}

        def f(splits: List[str]) -> Dict:
            rt = {}
            d = rt
            for n in splits:
                d[n] = {}
                d = d[n]

            d['#'] = 'done'
            return rt[splits[0]]

        for fld in folder:

            splits = fld[1:].split('/')
            d = trie

            for i, n in enumerate(splits):
                if n in d:
                    if '#' in d[n]:
                        break
                    if i == len(splits) - 1:
                        d[n] = {'#': 'done'}

                    d = d[n]

                else:
                    d[n] = f(splits[i:])
                    break

        res = []
        path = []

        # collect a subtree
        def collect(k: str, v: Dict):
            if '#' in v:
                res.append('/' + '/'.join(path + [k]))
                return

            for sd in v:
                path.append(k)
                collect(sd, v[sd])
                path.pop()

        for d in trie:
            collect(d, trie[d])

        return res


from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_folder = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, folder: str) -> bool:
        node = self.root
        parts = folder.split('/')
        is_new_folder = False

        for part in parts:
            if part not in node.children:
                node.children[part] = TrieNode()
                is_new_folder = True
            node = node.children[part]
            if node.is_end_of_folder:
                return False  # Subfolder detected

        node.is_end_of_folder = True
        return is_new_folder

class Solution1:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        result = []
        for f in sorted(folder):
            if trie.insert(f):
                result.append(f)
        return result


class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        last = res[0] + '/'
        for fld in folder[1:]:
            if fld.startswith(last):
                continue
            res.append(fld)
            last = fld + '/'

        return res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
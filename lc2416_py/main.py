

from typing import List

class Trie:
    def __init__(self):
        self.root = {'#': 0}

    def insert(self, s: str):
        curr = self.root
        for w in s:
            curr = curr.setdefault(w, {'#': 0})
            curr['#'] = curr.get('#', 0) + 1


    def dfs(self, s: str) -> int:
        curr = self.root
        tot = 0
        for w in s:
            if w not in curr:
                return tot
            tot += curr[w]['#']
            curr = curr[w]

        return tot


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        d = Trie()

        for w in words:
            d.insert(w)

        res = []
        for w in words:
            res.append(d.dfs(w))

        return res




class Trie1:
    def __init__(self):
        self.score = 0
        self.children = {}

    def add(self, s: str, i: int):
        if i:
            self.score += 1

        if i == len(s):
            return

        if not self.children.get(s[i]):
            self.children[s[i]] = Trie()

        self.children[s[i]].add(s, i + 1)

    def dfs(self, s: str, i: int):
        if i == len(s):
            return self.score
        return self.score + self.children[s[i]].dfs(s, i + 1)


class Solution1:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie1()
        for word in words:
            trie.add(word, 0)

        res = []
        for word in words:
            res.append(trie.dfs(word, 0))
        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
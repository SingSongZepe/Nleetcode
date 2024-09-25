

from typing import List

class Trie:
    def __init__(self):
      self.head = {'#': '?'}

    def insert(self, word: str) -> None:
      curr = self.head
      for l in word:
        curr = curr.setdefault(l, {})
      curr['#'] = '?'

    def search(self, word: str) -> bool:
        curr = self.head
        for l in word:
            if curr.get(l):
                curr = curr[l]
            else:
                return False
        return True if curr.get('#') else False


    def search_by_continuous(self, word: str) -> bool:
        curr = self.head
        for l in word:
            if curr.get(l) and curr.get('#'):
                curr = curr[l]
            else:
                return False
        return True if curr.get('#') else False

class Solution:
    def longestWord(self, words: List[str]) -> str:

        t = Trie()
        mx = ''

        for w in words:
            t.insert(w)

        for w in words:
            if t.search_by_continuous(w) and (len(w) > len(mx) or (len(w) == len(mx) and w < mx)):
                mx = w

        return mx




class Solution1:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        st = set([''])
        longest = ''

        for w in words:
            if w[:-1] in st:
                st.add(w)
                if len(w) > len(longest):
                    longest = w

        return longest



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
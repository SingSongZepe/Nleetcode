

class TrieNode:
    def __init__(self, val=''):
        self.val = ''
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        head = self.root
        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode(char)
            head = head.children[char]
        head.is_end_of_word = True

    def search(self, word: str) -> bool:
        head = self.root
        for char in word:
            if char not in head.children:
                return False
            head = head.children[char]
        return head.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for char in prefix:
            if char not in head.children:
                return False
            head = head.children[char]
        return True


class Trie1:
    def __init__(self):
      self.head = {}

    def insert(self, word: str) -> None:
      curr = self.head
      for l in word:
        curr = curr.setdefault(l, {})
      curr['#'] = '?'

    def search(self, word: str) -> bool:
      curr = self.head
      for l in word:
        if curr.get(l): # works becasue all dicts have something in them
          curr = curr[l]
        else:
          return False
      return True if curr.get('#') else False # works becasue all dicts have something in them

    def startsWith(self, prefix: str) -> bool:
      curr = self.head
      for l in prefix:
        if curr.get(l):
          curr = curr[l]
        else:
          return False
      return True




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
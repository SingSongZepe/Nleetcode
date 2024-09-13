

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(word) <= set(allowed) for word in words)

class Solution1:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(word) <= allowed for word in words)

class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed, count = set(allowed), 0
        for word in words:
            is_consistent = True
            for c in word:
                if c not in allowed:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1
        return count


def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List, Dict, Tuple, FrozenSet

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        d: Dict[Tuple, int] = {}
        tot = 0

        for w in words:
            tpl = tuple(sorted(set(w)))
            if tpl in d:
                tot += d[tpl]
                d[tpl] += 1
            else:
                d[tpl] = 1

        return tot


# use forzenset
class Solution:
    def similarPairs(self, words: List[str]) -> int:

        d: Dict[FrozenSet, int] = {}
        tot = 0

        for w in words:
            tpl = frozenset(w)
            if tpl in d:
                tot += d[tpl]
                d[tpl] += 1
            else:
                d[tpl] = 1

        return tot



        pass

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
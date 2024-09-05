

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        que = deque([startGene])
        mutations = 0

        while que:
            for _ in range(len(que)):
                gene = que.popleft()
                if gene == endGene:
                    return mutations

                # for i in range(len(gene)):
                #     for c in "ACGT":
                #         new_gene = gene[:i] + c + gene[i+1:]
                #         if new_gene in bank:
                #             que.append(new_gene)
                #             bank.remove(new_gene)

                tbank = bank.copy()
                for bgene in tbank:
                    if sum(1 for i in range(8) if gene[i] != bgene[i]) == 1:
                        que.append(bgene)
                        bank.remove(bgene)

            mutations += 1

        return -1


class Solution1:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bankSet = set(bank)

        q = deque()
        q.append(startGene)

        visited = set()
        visited.add(startGene)

        count = 0

        valid_set = {'A', 'C', 'G', 'T'}
        while q:
            for i in range(len(q)):
                gene = q.popleft()

                # no mutation
                if gene == endGene:
                    return count

                # compare bank
                candidate = bankSet.difference(visited)
                diff_cnt = 0
                for newGene in candidate:
                    diff_cnt = sum(1 for i in range(8) if gene[i] != newGene[i])
                    if diff_cnt == 1:
                        visited.add(newGene)
                        q.append(newGene)

            count += 1

        return -1



class Solution2:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        que = deque([startGene])
        mutations = 0

        while que:
            for _ in range(len(que)):
                gene = que.popleft()
                if gene == endGene:
                    return mutations

                tbank = bank.copy()
                for bgene in tbank:
                    if sum(1 for i in range(8) if gene[i] != bgene[i]) == 1:
                        que.append(bgene)
                        bank.remove(bgene)

            mutations += 1

        return -1


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
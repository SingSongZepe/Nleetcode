
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)

        # prefix and suffix check
        if all(s1[i] == s2[i] for i in range(n)) or all(s1[-i-1] == s2[-i-1] for i in range(n)):
            return True


        p1, p2 = -1, m
        for s in s2:
            if s == s1[p1+1]:
                p1 += 1
            else:
                break

        for s in s2[::-1]:
            if s == s1[p2-1]:
                p2 -= 1
            else:
                break

        if p2 < p1 or p1 == -1 or p2 == m or m + p1 - p2 +1 < n:
            return False


        return True


# better solution
class Solution1:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        i, j = 0, 0
        n, m = len(words1), len(words2)

        while i < n and i < m and words1[i] == words2[i]:
            i += 1

        while j < (n - i) and j < (m - i) and words1[n - j - 1] == words2[m - j - 1]:
            j += 1

        return i + j == n or i + j == m


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
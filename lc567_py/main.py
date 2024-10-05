

from collections import Counter

# hashmap
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if s1 is a substring of s2
        if len(s1) > len(s2):
            return False

        m, n = len(s1), len(s2)

        cnt = Counter(s1)
        window = Counter(s2[:m])
        if window == cnt:
            return True

        for i in range(m, n):
            window[s2[i-m]] -= 1
            window[s2[i]] += 1
            if window == cnt:
                return True

        return False

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if s1 is a substring of s2
        if len(s1) > len(s2):
            return False

        m, n = len(s1), len(s2)
        cnt = [0] * 26
        window = [0] * 26

        for i in range(m):
            cnt[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == cnt:
            return True

        for i in range(m, n):
            window[ord(s2[i-m]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] += 1
            if window == cnt:
                return True

        return False



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
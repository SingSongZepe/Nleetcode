
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        diff, dp1, dp2 = 0, None, None
        for (i, c1), c2 in zip(enumerate(s1), s2):
            if c1 != c2:
                diff += 1
                if dp1 is None:
                    dp1 = i
                else:
                    dp2 = i
                if diff > 2:
                    return False

        return diff == 0 or (diff == 2 and s1[dp1] == s2[dp2] and s1[dp2] == s2[dp1])



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
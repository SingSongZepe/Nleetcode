
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}
        m, n = len(s), len(p)

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= m and j >= n:
                return True
            if j >= n:
                return False

            if p[j] == '*':
                cache[(i, j)] = dfs(i, j+1) or (i < m and dfs(i+1, j))
                return cache[(i, j)]

            if p[j] == '?' or s[i] == p[j]:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == len(p) and len(p) == 0:
            return True
        if (len(s) != 0 and len(p) == 0):
            return False
        if p == "*":
            return True

        ls, rs = 0, 0
        patterns = p.split("*")

        for i, p in enumerate(patterns):
            if i == len(patterns) - 1 and p == "":
                return True
            elif i == 0 and p != "":
                rs += len(p)
                print(s[ls:rs], p)
                if not self.isSubstringMatch(s[ls:rs], p):
                    return False
                ls = rs
            elif p == "":
                continue
            elif i == len(patterns) - 1 and len(patterns) > 1:
                if ls == len(s) or len(s) - len(p) < ls:
                    return False
                ls = len(s) - len(p)
                rs = len(s) + 1
                return self.isSubstringMatch(s[ls:rs], p)
            else:
                rs += len(p)
                foundMatch = False
                while rs <= len(s):
                    if self.isSubstringMatch(s[ls:rs], p):
                        foundMatch = True
                        break
                    else:
                        ls += 1
                        rs += 1
                if not foundMatch:
                    return False
                ls = rs
        if ls != len(s):
            return False
        return True

    def isSubstringMatch(self, sub, p):
        print(sub, p)
        i = 0
        if len(sub) != len(p):
            return False
        while i < len(sub):
            if p[i] == "?" or sub[i] == p[i]:
                i += 1
                continue
            else:
                return False
        return True


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
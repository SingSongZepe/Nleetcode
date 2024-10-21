
class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        st = set()
        ml, n = 0, len(s)

        def dfs(cnt, i: int):
            nonlocal ml
            if ml >= cnt + n - i:
                return

            if i == n:
                ml = max(len(st), ml)

            for j in range(i+1, n+1):
                if s[i:j] in st:
                    continue
                st.add(s[i:j])
                dfs(cnt+1, j)
                st.remove(s[i:j])

        dfs(0, 0)
        return ml



def main():
    print('Hello World')

if __name__ == '__main__':
    main()


from typing import List, Set, Tuple


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        del_len = 26  # Initialize as infinity
        seen = set()

        def dfs(s: str, curr_del_len: int) -> None:
            nonlocal del_len

            # Optimization: if current deletion length is greater than the best found
            if curr_del_len > del_len:
                return

            # If we have already processed this string, return
            if s in seen:
                return
            seen.add(s)

            invalids = []
            open_stack = []
            close = []
            open = []

            for i, c in enumerate(s):
                if c == '(':
                    open_stack.append(i)
                    open.append(i)
                elif c == ')':
                    if not open_stack:
                        invalids.append(i)
                    else:
                        open_stack.pop()
                    close.append(i)

            invalids.extend(open_stack)  # Add invalid '(' indices

            if not invalids:
                # Found a valid string
                if curr_del_len < del_len:
                    res.clear()  # Clear the previous results
                    res.append(s)
                    del_len = curr_del_len
                elif curr_del_len == del_len:
                    res.append(s)
                return

            if open_stack:
                invalids.extend(open)
                invalids = set(invalids)
            else:
                invalids = set(close)
                invalids = set(invalids)


            # Try removing each invalid index
            for invalid in invalids:
                dfs(s[:invalid] + s[invalid + 1:], curr_del_len + 1)

        dfs(s, 0)  # Start DFS with 0 deletions
        return res


# optimize
class Solution1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        del_len = 26
        seen = set() # may be Set[Tuple[int,...]]

        def dfs(s: str, curr_del_len: int) -> None:
            nonlocal del_len

            if curr_del_len > del_len:
                return

            if s in seen:
                return
            seen.add(s)

            invalids = []
            open_stack = []
            close = []
            open = []
            last_char = ''

            for i, c in enumerate(s):
                if c == '(':
                    open_stack.append(i)
                    if last_char != '(':
                        open.append(i)
                elif c == ')':
                    if not open_stack:
                        invalids.append(i)
                    else:
                        open_stack.pop()

                    if last_char != ')':
                        close.append(i)

            invalids.extend(open_stack)

            if not invalids:
                if curr_del_len < del_len:
                    res.clear()
                    res.append(s)
                    del_len = curr_del_len
                elif curr_del_len == del_len:
                    res.append(s)
                return

            if open_stack:
                invalids.extend(open)
                invalids = set(invalids)
            else:
                invalids = set(close)
                invalids = set(invalids)

            for invalid in invalids:
                dfs(s[:invalid] + s[invalid + 1:], curr_del_len + 1)

        dfs(s, 0)
        return res


class Solution2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open_cnt = 0
        for c in s:
            if c == '(':
                open_cnt += 1
            elif c == ')':
                open_cnt -= 1

        def revert(s):
            reverse = [''] * len(s)
            for i, c in enumerate(s):
                reverse[-i - 1] = ')' if c == '(' else ('(' if c == ')' else c)
            return ''.join(reverse)

        if open_cnt > 0:
            return [revert(res) for res in self.removeInvalidParentheses(revert(s))]

        ans = []
        removes = [[]]
        closes = []
        open_cnt = 0
        consecutive = False
        last_valid = -1

        for i, c in enumerate(s):
            if c == '(':
                open_cnt += 1
            elif c == ')':
                open_cnt -= 1
                if not consecutive:
                    closes.append(i)
                if open_cnt < 0:
                    open_cnt = 0
                    new_removes = []

                    for re in removes:
                        lst = re[-1] if re else -1
                        idx = bisect_right(closes, lst)

                        for j in range(idx, len(closes)):
                            tmp = re[:]
                            tmp.append(closes[j])
                            new_removes.append(tmp)

                        if lst != - 1 and s[lst + 1] == ')':  # this can remove
                            re.append(lst + 1)
                            new_removes.append(re)

                    removes = new_removes

            consecutive = (c == ')')

            if open_cnt == 0:
                last_valid = i

        last = [""]
        if open_cnt > 0:
            last = self.removeInvalidParentheses(s[last_valid + 1:])

        for re in removes:
            tmp = list(s[:last_valid + 1])
            for i in re:
                tmp[i] = ''
            for lst in last:
                ans.append(''.join(tmp) + lst)
        return ans


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
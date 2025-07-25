
from typing import List, Set

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        prime_power_base = 1007
        modulus = 10000000007

        l, r = 0, min(len(path) for path in paths)
        shortest_length, shortest_mi = min([(len(path), mi) for mi, path in enumerate(paths)], key=lambda x: x[0])

        m = len(paths)

        def get_hashset(path: List[int], x: int) -> Set[int]:
            base_x = pow(prime_power_base, x, modulus)
            st = set()
            h = 0

            for i in range(x):
                h = (h * prime_power_base + path[i]) % modulus

            st.add(h)
            for i in range(x, len(path)):
                h = (h * prime_power_base - path[i - x] * base_x + path[i]) % modulus
                st.add(h)

            return st

        def has_common_path(x: int) -> bool:

            shortest_set = get_hashset(paths[shortest_mi], x)
            for mi in range(m):
                if mi == shortest_mi:
                    continue
                st = get_hashset(paths[mi], x)
                shortest_set = shortest_set & st

                if len(shortest_set) == 0:
                    return False

            return True

        res = 0
        while l <= r:
            mid = (l + r) // 2
            if has_common_path(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res

# maybe better when have no need to find the shortest one path
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        prime_power_base = 10007
        modulus = 100000000007

        l, r = 0, min(len(path) for path in paths)

        m = len(paths)

        def get_hashset(path: List[int], x: int) -> Set[int]:
            base_x = pow(prime_power_base, x, modulus)
            st = set()
            h = 0

            for i in range(x):
                h = (h * prime_power_base + path[i]) % modulus

            st.add(h)
            for i in range(x, len(path)):
                h = (h * prime_power_base - path[i - x] * base_x + path[i]) % modulus
                st.add(h)

            return st

        def has_common_path(x: int) -> bool:

            shortest_set = get_hashset(paths[0], x)
            for mi in range(1, m):
                st = get_hashset(paths[mi], x)
                shortest_set = shortest_set & st

                if len(shortest_set) == 0:
                    return False

            return True

        res = 0
        while l <= r:
            mid = (l + r) // 2
            if has_common_path(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
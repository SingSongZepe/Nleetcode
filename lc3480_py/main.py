

from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        left_bounding = [[] for _ in range(n)]
        for p1, p2 in conflictingPairs:
            p1, p2 = (p1, p2) if p1 < p2 else (p2, p1)
            left_bounding[p1-1].append(p2-1)

        base = 0
        right_bounding = [n, n]
        del_bonus = [0] * n

        # end with i
        for i in range(n-1, -1, -1):
            for l in left_bounding[i]:
                if l < right_bounding[0]:
                    right_bounding = [l, right_bounding[0]]
                elif l < right_bounding[1]:
                    right_bounding = [right_bounding[0], l]

            base += right_bounding[0] - i

            if right_bounding[0] < n:
                del_bonus[right_bounding[0]] += right_bounding[1] - right_bounding[0]

        return base + max(del_bonus)


# also a nice solution
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        n += 1
        conflictingPairs.sort(key=lambda p: max(*p))
        conflictingPairs.append([n, n])
        max_diff = 0
        max_left = 0
        rem = 0
        max_altleft = 0
        altrem = 0
        for l, r in conflictingPairs:
            if l > r:
                l,r=r,l
            if l > max_left:
                max_diff = max(
                    max_diff, (max_altleft - max_left) * (n - r) + rem - altrem
                )
                altrem = rem
                max_altleft = max_left
                rem += (l - max_left) * (n - r)
                max_left = l
            elif l > max_altleft:
                altrem += (l - max_altleft) * (n - r)
                max_altleft = l
        return (n - 1) * n // 2 - rem + max_diff


def main():
    print('Hello World')

if __name__ == '__main__':
    main()

from typing import List, Dict, Optional
from collections import defaultdict

class Solution:
    def bs_greater_than(self, arr, val) -> Optional[int]:
        left, right = 0, len(arr) - 1
        result = None
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > val:
                result = arr[mid]
                right = mid - 1
            else:
                left = mid + 1
        return result

    def bs_less_than(self, arr, val) -> Optional[int]:
        left, right = 0, len(arr) - 1
        result = None
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < val:
                result = arr[mid]
                left = mid + 1
            else:
                right = mid - 1
        return result

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, d, md = 0, 0, 0, 0
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x_obs: Dict[int, List[int]] = defaultdict(list)
        y_obs: Dict[int, List[int]] = defaultdict(list)
        for obs in obstacles:
            x_obs[obs[0]].append(obs[1])
            y_obs[obs[1]].append(obs[0])

        for key in x_obs:
            x_obs[key].sort()
        for key in y_obs:
            y_obs[key].sort()

        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                if d == 0:
                    ym = self.bs_greater_than(x_obs[x], y)
                    if ym is not None:
                        y = min(ym-1, y + cmd)
                    else:
                        y += cmd
                elif d == 2:
                    ym = self.bs_less_than(x_obs[x], y)
                    if ym is not None:
                        y = max(ym+1, y - cmd)
                    else:
                        y -= cmd
                elif d == 1:
                    xm = self.bs_greater_than(y_obs[y], x)
                    if xm is not None:
                        x = min(xm-1, x + cmd)
                    else:
                        x += cmd
                else:
                    xm = self.bs_less_than(y_obs[y], x)
                    if xm is not None:
                        x = max(xm+1, x - cmd)
                    else:
                        x -= cmd
                md = max(md, x ** 2 + y ** 2)

        return md












        pass



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
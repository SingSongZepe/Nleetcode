

from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        cnt = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(cnt)]

        #      curr       fuel left   loc-finish total count
        def dfs(loc: int, fuel: int) -> int:
            tot = 0
            if loc == finish:
                tot += 1

            for nloc in range(cnt):
                if nloc == loc:
                    continue
                nfuel = fuel - abs(locations[nloc] - locations[loc])
                if nfuel < 0:
                    continue

                if dp[nloc][nfuel] == -1:
                    tot += dfs(nloc, nfuel)
                else:
                    tot += dp[nloc][nfuel]

            dp[loc][fuel] = tot
            return tot

        return dfs(start, fuel) % (10**9 + 7)












        pass



class Solution1:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1] * (fuel + 1) for _ in range(len(locations))]

        def helper(location, fuel_left):
            total = 0
            if location == finish:
                total += 1
            for i in range(len(locations)):
                if i == location:
                    continue
                k = fuel_left - abs(locations[i] - locations[location])
                if k < 0:
                    continue
                if dp[i][k] == -1:
                    total += helper(i , k)
                else:
                    total += dp[i][k]
            dp[location][fuel_left] = total
            return total

        return helper(start, fuel) % (pow(10, 9) + 7)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
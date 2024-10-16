
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = ''

        while pq:
            cnt1, c1 = heapq.heappop(pq)

            if len(result) >= 2 and result[-2:] == c1 * 2:
                if not pq:
                    break

                cnt2, c2 = heapq.heappop(pq)
                result += c2
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(pq, (cnt2, c2))

                heapq.heappush(pq, (cnt1, c1))

            else:
                result += c1
                cnt1 += 1

                if cnt1 < 0:
                    heapq.heappush(pq, (cnt1, c1))

        return result


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
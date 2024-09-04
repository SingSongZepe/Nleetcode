

from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start > destination:
            start, destination = destination, start

        td = sum(distance[start:destination])
        return min(td, sum(distance) - td)



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
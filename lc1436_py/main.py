

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_cities = set()
        cities = set()

        for path in paths:
            from_cities.add(path[0])
            cities.add(path[1])

        return (cities - from_cities).pop()




def main():
    print('Hello World')

if __name__ == '__main__':
    main()
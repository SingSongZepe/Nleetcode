

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        threshold = 0
        for bp in batteryPercentages:
            if bp <= threshold:
                continue
            threshold += 1

        return threshold


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
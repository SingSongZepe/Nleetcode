

from collections import defaultdict

## simple implementation of AllOne data structure
## O(1) time complexity for both inc and dec operations, but O(n) time for getMaxKey and getMinKey operations
## O(n) space complexity for storing all keys and their frequencies
class AllOne:

    def __init__(self):
        self.freq = defaultdict(int)

    def inc(self, key: str) -> None:
        self.freq[key] += 1


    def dec(self, key: str) -> None:
        if self.freq[key] > 0:
            self.freq[key] -= 1


    def getMaxKey(self) -> str:
        if self.freq:
            max_freq = max(self.freq.values())
            for key, freq in self.freq.items():
                if freq == max_freq:
                    return key

            return ''


    def getMinKey(self) -> str:
        if self.freq:
            min_freq = float('inf')
            for freq in self.freq.values():
                if freq < min_freq and freq > 0:
                    min_freq = freq
            for key, freq in self.freq.items():
                if freq == min_freq:
                    return key

            return ''


## cache implementation of AllOne data structure

class AllOne1:

    def __init__(self):
        self.freq = defaultdict(int)
        self.op = 0
        self.res = ''

    def inc(self, key: str) -> None:
        self.freq[key] += 1
        self.op = 0

    def dec(self, key: str) -> None:
        if self.freq[key] > 0:
            self.freq[key] -= 1
            self.op = 0

    def getMaxKey(self) -> str:
        if self.op == 1:
            return self.res
        self.op = 1
        if self.freq:
            max_freq = max(self.freq.values())
            for key, freq in self.freq.items():
                if freq == max_freq:
                    self.res = key
                    return key

        return ''


    def getMinKey(self) -> str:
        if self.op == 2:
            return self.res
        self.op = 2
        if self.freq:
            min_freq = float('inf')
            for freq in self.freq.values():
                if freq < min_freq and freq > 0:
                    min_freq = freq
            for key, freq in self.freq.items():
                if freq == min_freq:
                    self.res = key
                    return key

        return ''


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
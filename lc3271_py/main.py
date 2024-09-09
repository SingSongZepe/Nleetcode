
class Solution:
    def stringHash(self, s: str, k: int) -> str:

        def get_value(s: str) -> int:
            return sum(ord(c) for c in s) - len(s) * ord('a')

        res = ''
        for i in range(0, len(s), k):
            res += chr((get_value(s[i:i+k])) % 26 + ord('a'))

        return res



from string import ascii_lowercase

class Solution1:
    def stringHash(self, s: str, k: int) -> str:
        value = [ord(ch) - 97 for ch in s]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        return ''.join([alphabet[sum(value[i:i + k]) % 26] for i in range(0, len(value), k)])





def get_value(s: str) -> int:
    return sum(ord(c) for c in s) - len(s) * ord('a')

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
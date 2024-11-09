
class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        for c in word:
            if not c.isalnum():
                return False
            if c.isdigit():
                continue
            if not has_vowel and c in 'aeiouAEIOU':
                has_vowel = True
            elif not has_consonant and c not in '0123456789aeiouAEIOU':
                has_consonant = True

        return has_vowel and has_consonant











        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()
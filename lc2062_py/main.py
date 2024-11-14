
class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        cnt = 0
        vowel_st = {'a', 'e', 'i', 'o', 'u'}
        st = set()
        word += ' '

        l = 0
        for r in range(len(word)):
            rc = word[r]
            if rc in vowel_st:
                st.add(rc)
            else:  # [l, r]
                if len(st) == 5:
                    for i in range(l, r):
                        vowel = set()
                        for j in range(i, r):  #[i, j]
                            if word[j] in vowel_st:
                                vowel.add(word[j])
                            if len(vowel) == 5:
                                cnt += 1
                l = r + 1
                st = set()

        return cnt





def main():
    print('Hello World')

if __name__ == '__main__':
    main()
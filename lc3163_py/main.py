
class Solution:
    def compressedString(self, word: str) -> str:

        l, r = 0, 0
        comp = []
        while r < len(word)-1:
            cnt = r-l+1
            if word[r] == word[r+1] and cnt < 9:
                r += 1
                continue
            comp.append(str(cnt)+word[r])
            r += 1
            l = r

        return comp + str(r-l+1) + word[r]


class Solution1:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        comp = []
        current_char = word[0]
        count = 1

        for c in word[1:]:
            if c == current_char:
                if count == 9:
                    comp.append("9")
                    comp.append(current_char)
                    count = 1
                else:
                    count += 1
            else:
                comp.append(str(count))
                comp.append(current_char)
                current_char = c
                count = 1

        # Append the last run
        comp.append(str(count))
        comp.append(current_char)

        return ''.join(comp)













        pass






def main():
    print('Hello World')

if __name__ == '__main__':
    main()
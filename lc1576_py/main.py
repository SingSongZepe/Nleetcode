

from string import ascii_lowercase

class Solution:
    def modifyString(self, s: str) -> str:

        remain = set(ascii_lowercase) - set(s)

        for i in range(len(s)):
            if s[i] == '?':
                s = s[:i] + remain.pop() + s[i+1:]

        return s


class Solution1:
    def modifyString(self, s: str) -> str:
        al='abcdefghijklmnoppqrstuvwxyz'
        d=[]
        for i in range(len(s)):
            if s[i]=='?':
                d.append(i)
        if len(s)==1:
            return 'a'
        for i in d:
            if i==0 and len(s)!=1:
                for k in al:
                    if s[1]!=k:
                        s=k+s[i+1:]
                        break
            elif i==len(s)-1:
                for k in al:
                    if s[i-1]!=k:
                        s=s[:i]+k
                        break
            elif i>0 and i<len(s)-1:
                for k in al:
                    if s[i-1]!=k and s[i+1]!=k:
                        s=s[:i]+k+s[i+1:]
                        break
        return s


class Solution2:
    def modifyString(self, s: str) -> str:
        al=set(ascii_lowercase)
        d=[]
        for i in range(len(s)):
            if s[i]=='?':
                d.append(i)
        if len(s)==1:
            return 'a'
        for i in d:
            if i==0 and len(s)!=1:
                s=(al-set(s[1])).pop() + s[1:]
            elif i==len(s)-1:
                s=s[:i] + (al-set(s[i-1])).pop()
            elif i>0 and i<len(s)-1:
                s=s[:i] + (al-set(s[i-1])-set(s[i+1])).pop() + s[i+1:]
        return s

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
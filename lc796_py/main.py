

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        m, n = len(s), len(goal)
        if m != n:
            return False

        if set(s) != set(goal):
            return False

        for i in range(m):
            if s[i+1:] + s[:i+1] == goal:
                return True

        return False



def main():
    print('Hello World')

if __name__ == '__main__':
    main()
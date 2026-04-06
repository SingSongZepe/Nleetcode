#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

class Solution {
public:
    int mark(const string& s, int l, int r) { // [l, r)
        if (r - l <= 2) return 1;

        int left_brace = 0;
        int total_mark = 0;

        int left_brace_idx = l+1;
        for (int i = l+1; i < r-1; i++) {
            if (s[i] == '(') left_brace++;
            else if (s[i] == ')') {
                left_brace--;
                if (!left_brace) {
                    total_mark += mark(s, left_brace_idx, i+1);
                    left_brace_idx = i+1;
                }
            }
        }

        return 2 * total_mark;
    }
    int scoreOfParentheses(string s) {
        s = '(' + s + ')';
        return mark(s, 0, s.size()) / 2;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    string s = "()()";
    result = sol->scoreOfParentheses(s);
    std::cout << result << std::endl;

    return 0;
}

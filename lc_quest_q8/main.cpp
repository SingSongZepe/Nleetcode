#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

typedef long long LL;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

template <typename T>
void print_vector_ln(const vector<T>& v) {
    print_vector(v); std::cout << "\n";
}

template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

// leetcode tree node
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <stack>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        auto get_op_idx = [](const string& s) { // 0 is number 1~4 +-*/
            if (s == "+") return 1;
            if (s == "-") return 2;
            if (s == "*") return 3;
            if (s == "/") return 4;
            return 0;
        };

        std::stack<int> data;
        for (const auto& token : tokens) {
            int op_idx = get_op_idx(token);
            if (op_idx) {
                int b = data.top(); data.pop();
                int a = data.top(); data.pop();
                switch (op_idx) {
                case 1:
                    data.push(a + b); break;
                case 2:
                    data.push(a - b); break;
                case 3:
                    data.push(a * b); break;
                case 4:
                    data.push(a / b); break;
                default: break;
                }
            } else data.push(std::atoi(token.c_str()));
        }

        return data.top();
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

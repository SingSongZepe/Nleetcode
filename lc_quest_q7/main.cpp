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


class Solution {
public:
    const string push    = "Push";
    const string pop     = "Pop";
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ops;
        int curr = 1;
        for (const int t : target) {
            while (curr < t) {
                ops.emplace_back(push);
                ops.emplace_back(pop);
                curr++;
            }
            ops.emplace_back(push);
            curr++;
        }

        return ops;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    vector<string> result;

    vector<int> target;

    target = {1, 3};
    n = 3;    
    result = sol->buildArray(target, n);
    print_vector_ln(result);

    target = {1, 2, 3};
    n = 3;    
    result = sol->buildArray(target, n);
    print_vector_ln(result);

    target = {1, 2};
    n = 4;    
    result = sol->buildArray(target, n);
    print_vector_ln(result);

    target = {1, 99};
    n = 100;    
    result = sol->buildArray(target, n);
    print_vector_ln(result);

    return 0;
}

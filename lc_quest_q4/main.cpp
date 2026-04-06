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
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int target = n * (n+1) / 2;
        int actual = 0;
        
        vector<int> st(n+1, 0);
        int dup = 0;
        for (const int num : nums) {
            st[num] += 1;
            actual += num;
            if (st[num] > 1) dup = num;
        }
        
        int t = target - actual + dup;
        return {dup, t};
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

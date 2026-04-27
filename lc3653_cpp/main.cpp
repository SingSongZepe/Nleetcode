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
    typedef long long LL;
    const int MOD = 1e9 + 7;
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        for (const auto& query : queries) {
            int l = query[0], r = query[1], k = query[2], v = query[3];
            if (v == 1) continue;
            for (int idx = l; idx <= r; idx += k) {
                nums[idx] = ((LL)nums[idx] * (LL)v) % MOD;
            }
        }
        int res = 0;
        for (const int num : nums) {
            res ^= num;
        }
        return res;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

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

// non in-place
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res(2*n, 0);
        for (int i = 0; i < n; i++) {
            res[2*i] = nums[i];
            res[2*i+1] = nums[n+i];
        }
        return res;
    }
};

// in-place 1
class Solution1 {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        for (int i = 0; i < n; i++) {
            nums[2*i]   |= ((nums[i] & 1023) << 10);
            nums[2*i+1] |= ((nums[n+i] & 1023) << 10);
        }
        for (int i = 0; i < 2 * n; i++) {
            nums[i] >>= 10;
        }
        return nums;
    }
};

int main() 
{
    // int a = 3;
    // int b = 5;
    // a &= 
    // std::cout << 
    // return 0;
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

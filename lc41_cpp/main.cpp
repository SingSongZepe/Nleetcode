#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;
using std::max;
using std::min;

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

#include <unordered_set>
class Solution1 {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        std::unordered_set<int> st;
        for (const int num : nums) if (0 < num && num <= n) st.emplace(num);
        for (int i = 1; ; i++) {
            if (!st.count(i)) return i;
        }
        throw std::runtime_error("unreachable!");
    }
};

#include <unordered_set>
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (0 < nums[i] && nums[i] <= n && nums[i] != i+1 && nums[nums[i]-1] != nums[i]) {
                std::swap(nums[i], nums[nums[i]-1]);
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i+1) return i+1; 
        }
        return n+1;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> nums;
    
    nums = {1, 2, 0};
    result = sol->firstMissingPositive(nums);
    std::cout << result << std::endl;

    nums = {3, 4, -1, 1};
    result = sol->firstMissingPositive(nums);
    std::cout << result << std::endl;

    nums = {1};
    result = sol->firstMissingPositive(nums);
    std::cout << result << std::endl;

    nums = {1, 1};
    result = sol->firstMissingPositive(nums);
    std::cout << result << std::endl;

    return 0;
}

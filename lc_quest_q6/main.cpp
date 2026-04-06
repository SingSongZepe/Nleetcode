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

// non-in-place
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> count(nums.size()+1, 0);
        for (const int num : nums) count[num]++;
        vector<int> res;
        for (int i = 1; i <= nums.size(); i++) if (!count[i]) res.emplace_back(i);
        return res;
    }
};

// in-place
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int p = nums[i];
            while (p != 0) {
                int op = p;
                p = nums[p-1];
                nums[op-1] = 0;
            }
        }

        vector<int> res;
        for (int i = 0; i < nums.size(); i++) if (nums[i] != 0) res.emplace_back(i+1);
        return res;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    vector<int> result;
    
    vector<int> nums;

    nums = {4, 3, 2, 7, 8, 2, 3, 1};
    result = sol->findDisappearedNumbers(nums);
    print_vector(result);

    nums = {1, 1};
    result = sol->findDisappearedNumbers(nums);
    print_vector(result);

    return 0;
}

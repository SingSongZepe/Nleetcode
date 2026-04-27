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

#include <unordered_map>
#include <algorithm>
#include <limits>
class Solution1 {
public:
    const int MAX = std::numeric_limits<int>::max();
    int minimumDistance(vector<int>& nums) {
        std::unordered_map<int, vector<int>> same_vals;
        for (int i = 0; i < nums.size(); i++) same_vals[nums[i]].emplace_back(i);
        int min_dist = MAX;
        for (auto& [_, vals] : same_vals) {
            if (vals.size() < 3) continue;
            for (int i = 1; i < vals.size()-1; i++) {
                min_dist = std::min(min_dist, vals[i+1]-vals[i-1]);
            }
            if (min_dist == 2) return 4;
        }
        return min_dist == MAX ? -1 : 2*min_dist;
    }
};

class Solution {
public:
    const int MAX = std::numeric_limits<int>::max();
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        // record the last 2 position of a distinct number
        // pos_rec[0][num] means first last one
        // pos_rec[1][num] means second last one
        vector<vector<int>> pos_rec(2, vector<int>(n, -1));
        int min_dist = MAX;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i] - 1; // nums[i] in range [1, n], remap it to [0, n-1]
            if (pos_rec[1][num] != -1) min_dist = std::min(min_dist, i - pos_rec[1][num]);
            pos_rec[1][num] = pos_rec[0][num];
            pos_rec[0][num] = i;
        }
        return min_dist == MAX ? -1 : 2*min_dist;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> nums;
    
    nums = {1, 2, 1, 1, 3};
    result = sol->minimumDistance(nums);
    std::cout << result << std::endl;

    nums = {1,1,2,3,2,1,2};
    result = sol->minimumDistance(nums);
    std::cout << result << std::endl;

    return 0;
}

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


#include <deque>
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        // pair
        std::deque<uint32_t> q;
        
        vector<int> res;
        res.reserve(n-k+1);

        for (int i = 0; i < n; i++) {
            while (!q.empty() && nums[q.back()] < nums[i]) {
                q.pop_back();
            } q.emplace_back(i);
            if (q.front() == i - k) q.pop_front();
            if (i >= k-1) res.emplace_back(nums[q.front()]);
        }
        return res;
    }
};


// a better solution
class Solution1 {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result;
        
        if (n == 0 || k == 0) {
            return result;
        }
        
        if (k == 1) {
            return nums;
        }
        
        int num_windows = n - k + 1;
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        
        left[0] = nums[0];
        right[n - 1] = nums[n - 1];
        
        for (int i = 1; i < n; ++i) {
            if (i % k == 0) {
                left[i] = nums[i];
            } else {
                left[i] = std::max(nums[i], left[i - 1]);
            }
            
            int endIdx = n - i - 1;
            
            if ((endIdx + 1) % k == 0) {
                right[endIdx] = nums[endIdx];
            } else {
                right[endIdx] = std::max(right[endIdx + 1], nums[endIdx]);
            }
        }
        
        result.resize(num_windows); // num of windows
        
        for (int i = 0; i < num_windows; ++i) {
            result[i] = std::max(left[i + k - 1], right[i]);
        }
        
        return result;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    vector<int> result;

    vector<int> nums;
    int k;

    nums = {1, 3, -1, -3, 5, 3, 6, 7};
    k = 3;
    result = sol->maxSlidingWindow(nums, k);
    print_vector_ln(result);

    return 0;
}

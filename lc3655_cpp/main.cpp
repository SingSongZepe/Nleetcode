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

#include <cmath>
#include <unordered_map>
class Solution {
public:
    typedef long long LL;
    const int MOD = 1e9 + 7;

    LL quick_pow(LL a, LL b) {
        LL res = 1;
        a %= MOD;
        while (b) {
            if (b & 1) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int B = sqrt(n);
        
        vector<vector<vector<int>>> groups(B + 1);
        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            if (k <= B) {
                groups[k].push_back({l, r, v});
            } else {
                for (int i = l; i <= r; i += k) {
                    nums[i] = (LL)nums[i] * v % MOD;
                }
            }
        }

        vector<LL> diff(n + B + 10);

        for (int k = 1; k <= B; ++k) {
            if (groups[k].empty()) continue;
            
            fill(diff.begin(), diff.end(), 1);
            for (auto& op : groups[k]) {
                int l = op[0], r = op[1], v = op[2];
                diff[l] = diff[l] * v % MOD;
                int rb = ((r - l) / k + 1) * k + l;
                if (rb < diff.size()) {
                    diff[rb] = diff[rb] * quick_pow(v, MOD - 2) % MOD;
                }
            }

            for (int i = k; i < n; ++i) {
                diff[i] = diff[i] * diff[i - k] % MOD;
            }
            for (int i = 0; i < n; ++i) {
                nums[i] = (LL)nums[i] * diff[i] % MOD;
            }
        }

        int res = 0;
        for (int x : nums) res ^= x;
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

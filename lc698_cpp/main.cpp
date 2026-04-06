#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

#include <algorithm>
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for (const int num : nums) {
            sum += num;
        }
        if (sum % k != 0) return false;
        int target = sum / k;

        std::sort(nums.rbegin(), nums.rend());
        if (nums[0] > target) return false;

        vector<int> buckets(k, 0);
        return dfs(nums, 0, buckets, target);
    }

    bool dfs(const vector<int>& nums, int idx, vector<int>& buckets, const int target) {
        if (idx >= nums.size()) return true;
        for (int i = 0; i < buckets.size(); i++) {
            if (i > 0 && buckets[i] == buckets[i-1]) continue;
            // place the num into buckets[i]
            if (buckets[i] + nums[idx] <= target) {
                buckets[i] += nums[idx];
                if (dfs(nums, idx + 1, buckets, target)) return true;
                buckets[i] -= nums[idx];
            }
            
            if (buckets[i] == 0) break;
        }
        // the current nums[idx] has no bucket to go,
        // so match failed.
        return false;
    }
};

class Solution1 {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for (const int num : nums) {
            sum += num;
        }
        if (sum % k != 0) return false;
        int target = sum / k;
        
        // dp[mask] means the current number inside the last buckets use
        // `mask` numbers, where mask is divide to n bit, and 1 means the number is used, otherwise is not used
        int n = nums.size();
        vector<int> dp(1 << n, -1);
        dp[0] = 0;

        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            for (int i = 0; i < n; i++) {
                if (!((mask >> i) & 1)) {
                    if (dp[mask] + nums[i] <= target) {
                        dp[mask|(1 << i)] = (dp[mask] + nums[i]) % target;
                    } // otherwise nums[i] can't be put in the last bucket
                }
            }
            if (dp[(1 << n)-1] == 0) return true;
        }
        return dp[(1 << n)-1] == 0;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    auto sol1 = std::make_unique<Solution1>();
    
    int n;
    int result;

    vector<int> nums;
    int k;

    // Solution 1
    // dfs
    nums = {4, 3, 2, 3, 5, 2, 1};
    k = 4;
    result = sol->canPartitionKSubsets(nums, k);
    std::cout << result << std::endl;

    nums = {1, 2, 3, 4};
    k = 3;
    result = sol->canPartitionKSubsets(nums, k);
    std::cout << result << std::endl;

    // Solution 2
    // bitmask DP
    // dp[mask]
    nums = {4, 3, 2, 3, 5, 2, 1};
    k = 4;
    result = sol1->canPartitionKSubsets(nums, k);
    std::cout << result << std::endl;

    nums = {1, 2, 3, 4};
    k = 3;
    result = sol1->canPartitionKSubsets(nums, k);
    std::cout << result << std::endl;


    return 0;
}

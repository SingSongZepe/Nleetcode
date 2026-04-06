#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;

// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         int n = nums.size();
//         // dp[i][0], the max amount if not robs house_i
//         // dp[i][1], the max amound if robs house_i
//         vector<vector<int>> dp(n, vector<int>(2));
//         dp[0][0] = 0;
//         dp[0][1] = nums[0];

//         for (int i = 1; i < n; i++) {
//             dp[i][0] = std::max(dp[i-1][0], dp[i-1][1]);
//             dp[i][1] = dp[i-1][0] + nums[i];
//         }

//         return std::max(dp[n-1][0], dp[n-1][1]);
//     }
// };

// better, space optimization
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        // dp[0], the max amount if not robs house_i
        // dp[1], the max amound if robs house_i
        int dp[2];
        dp[0] = 0;
        dp[1] = nums[0];

        for (int i = 1; i < n; i++) {
            int old_dp[2];
            memcpy(old_dp, dp, sizeof(dp));

            dp[0] = std::max(old_dp[0], old_dp[1]);
            dp[1] = old_dp[0] + nums[i];
        }

        return std::max(dp[0], dp[1]);
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    vector<int> nums = {2, 3, 2};
    int result;

    result = sol->rob(nums);
    std::cout << result << "\n";

    return 0;
}

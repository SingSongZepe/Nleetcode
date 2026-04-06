#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        
        int n = nums.size();
        // dp[i][0], the max amount if not robs house_i
        // dp[i][1], the max amound if robs house_i
        int dp[2];
        memset(dp, 0x00, sizeof(dp));

        for (int i = 0; i < nums.size()-1; i++) {
            int odp[2];
            memcpy(odp, dp, sizeof(dp));

            dp[0] = std::max(odp[0], odp[1]);
            dp[1] = odp[0] + nums[i]; 
        }

        int curr_max = std::max(dp[0], dp[1]);

        memset(dp, 0x00, sizeof(dp));

        for (int i = 1; i < nums.size(); i++) {
            int odp[2];
            memcpy(odp, dp, sizeof(dp));

            dp[0] = std::max(odp[0], odp[1]);
            dp[1] = odp[0] + nums[i]; 
        }

        return std::max(std::max(dp[0], dp[1]), curr_max);
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

    printf("Hello World!");

    return 0;
}

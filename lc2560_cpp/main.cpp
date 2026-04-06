#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <limits>

using std::vector;
using std::string;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

class Solution {
public:
    // or inline 
    inline bool check(const vector<int>& nums, int mid, int k) {
        int count = 0;
        int stole = false;
        for (const int num : nums) {
            if (num <= mid && !stole) {
                count++;
                stole = !stole;
            } else stole = false;
            if (count >= k) return true;
        }
        return false;
    }
    int minCapability(vector<int>& nums, int k) {
        
        int maxCap = 0;
        int minCap = std::numeric_limits<int>::max(); 
        for (const int num : nums) {
            if (num > maxCap) maxCap = num;
            if (num < minCap) minCap = num;
        }
        // or 
        // int maxCap = 1e9;
        // int minCap = 1;

        int n = nums.size();
        // dp check
        // auto check = [&](int mid) {
        //     // dp[i][0] means the previous i house can offers if do not rob the current house
        //     // dp[i][1] means the previous i house can offers if rob the current house
        //     int dp[2];
        //     memset(dp, 0x00, sizeof(dp));
        //     for (int i = 1; i <= n; i++) {
        //         int odp[2];
        //         memcpy(odp, dp, sizeof(dp)); 

        //         int stealable = mid >= nums[i-1] ? 1 : 0;
        //         dp[0] = std::max(odp[1], odp[0]);
        //         dp[1] = odp[0] + stealable;
                
        //         if (dp[0] >= k || dp[1] >= k) return true;
        //     }

        //     return dp[0] >= k || dp[1] >= k;
        // };

        // greedy check
        // auto check = [&](int mid) {
        //     int count = 0;
        //     int stole = false;
        //     for (const int num : nums) {
        //         if (num <= mid && !stole) {
        //             count++;
        //             stole = !stole;
        //         } else stole = false;
        //         if (count >= k) return true;
        //     }
        //     return false;
        // };

        // bisect
        int l = minCap; int r = maxCap;
        while (l < r) {
            int mid = (l + r) >> 1;
            // std::cout << mid << " ";
            if (check(nums, mid, k)) { // if mid is valid
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        
        return r;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> nums;
    int k;

    nums = {2, 3, 5, 9};
    k = 2;
    result = sol->minCapability(nums, k);
    std::cout << result << std::endl;

    nums = {2, 7, 9, 3, 1};
    k = 2;
    result = sol->minCapability(nums, k);
    std::cout << result << std::endl;

    return 0;
}

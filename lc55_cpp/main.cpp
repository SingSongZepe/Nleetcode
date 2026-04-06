#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

// class Solution {
// public:
//     bool canJump(vector<int>& nums) {
//         int n = nums.size();
//         if (n <= 1) return true;

//         int curr = 0;
//         while (curr < n - 1) {
//             if (nums[curr] == 0) return false;

//             int maxReach = 0;
//             int next_curr = curr;
//             for (int i = 1; i <= nums[curr]; i++) {
//                 int target = curr + i; 
//                 if (target >= n-1) return true;

//                 if (target + nums[target] > maxReach) {
//                     maxReach = target + nums[target];
//                     next_curr = target;
//                 }
//             }
//             curr = next_curr;
//         }
//         return true;
//     }
// };

// obviously better algo
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > maxReach) return false;
            maxReach = std::max(maxReach, i + nums[i]);
        }
        return true;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    vector<int> nums{2, 3, 1, 1, 4};
    result = sol->canJump(nums);
    std::cout << result << "\n";

    return 0;
}

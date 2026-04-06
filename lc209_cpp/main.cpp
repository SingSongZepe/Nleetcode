#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <limits>

using std::vector;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int currSum = 0;

        int l = 0;
        int minlen = std::numeric_limits<int>::max();
        for (int r = 0; r < nums.size(); r++) {
            currSum += nums[r];
            while (l <= r && currSum >= target) {
                minlen = std::min(minlen, r - l + 1);
                currSum -= nums[l];
                l++;
            }
        }

        return minlen == std::numeric_limits<int>::max() ? 0 : minlen;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();

    int target;
    vector<int> nums;
    int result;

    target = 7;
    nums = {2, 3, 1, 2, 4, 3};
    result = sol->minSubArrayLen(target, nums);
    std::cout << result << std::endl;

    target = 4;
    nums = {1, 4, 4};
    result = sol->minSubArrayLen(target, nums);
    std::cout << result << std::endl;

    target = 11;
    nums = {1,1,1,1,1,1,1,1};
    result = sol->minSubArrayLen(target, nums);
    std::cout << result << std::endl;

    return 0;
}

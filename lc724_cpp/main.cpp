#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> presum(n+1, 0);

        for (int i = 0; i < n; i++) {
            presum[i+1] = presum[i] + nums[i];
        }

        for (int i = 0; i < n; i++) {
            if (presum[n] - 2 * presum[i] == nums[i]) return i;
        }

        return -1;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;



    return 0;
}

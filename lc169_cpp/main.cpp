#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int maj = nums[0];
        int c = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (c == 0) {
                maj = nums[i];
                c = 1;
            } else {
                if (maj == nums[i]) c++; 
                else c--;
            }
        }
        return maj;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    std::vector<int> input; 
    int result;

    input = {3, 2, 3};
    result = sol->majorityElement(input);
    std::cout << result << std::endl;

    input = {2, 2, 1, 1, 1, 2, 2};
    result = sol->majorityElement(input);
    std::cout << result << std::endl;

    return 0;
}

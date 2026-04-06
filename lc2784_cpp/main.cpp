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

#define N 105
class Solution {
public:
    bool isGood(vector<int>& nums) {
        int cnt[N];
        memset(cnt, 0x00, sizeof(cnt));

        int n = nums.size();
        for (const int num : nums) {
            if (num > n-1) {
                return false;
            }
            if (num != n-1 && cnt[num] > 0) { // num already exist
                return false;
            }
            cnt[num]++;
        }
        return cnt[n-1] == 2;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    vector<int> nums;
    
    nums = {2, 1, 3};
    result = sol->isGood(nums);
    std::cout << result << std::endl;

    nums = {1, 3, 3, 2};
    result = sol->isGood(nums);
    std::cout << result << std::endl;

    nums = {1, 1};
    result = sol->isGood(nums);
    std::cout << result << std::endl;

    nums = {3, 4, 4, 1, 2, 1};
    result = sol->isGood(nums);
    std::cout << result << std::endl;


    return 0;
}

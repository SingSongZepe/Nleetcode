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
    vector<int> maxKDistinct(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), [](const int& a, const int& b) {
            return a > b;
        });

        vector<int> result{nums[0]};
        k--;
        for (int i = 1; i < nums.size() && k; i++) {
            if (nums[i] != nums[i-1]) {
                k--;
                result.emplace_back(nums[i]);
            }
        }

        return result;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    vector<int> result;

    vector<int> nums{84,93,100,77,93};
    int k = 3;
    result = sol->maxKDistinct(nums, k);
    print_vector(result);

    return 0;
}

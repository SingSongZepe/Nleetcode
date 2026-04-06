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
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> res(nums.size(), 0);
        int l = 0, r = nums.size()-1;
        
        for (const int num : nums) {
            if (num < pivot) {
                res[l++] = num;
            } else if (num > pivot) {
                res[r--] = num;
            }
        }
        while (l <= r) res[l++] = pivot;
        // reverse r+1 .. n
        reverse(res.begin() + r+1, res.end());
        
        return res;
    }
};

// better and more intuitive
// but thrice iterate
class Solution1 {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> res(nums.size());
        int i = 0;
        
        for (int x : nums) if (x < pivot) res[i++] = x;
        for (int x : nums) if (x == pivot) res[i++] = x;
        for (int x : nums) if (x > pivot) res[i++] = x;
        
        return res;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    vector<int> result;

    vector<int> nums;
    int pivot;

    nums = {9, 12, 5, 10, 14, 3, 10};
    pivot = 10;
    result = sol->pivotArray(nums, pivot);
    print_vector(result);

    nums = {-3, 4, 3, 2};
    pivot = 2;
    result = sol->pivotArray(nums, pivot);
    print_vector(result);

    return 0;
}

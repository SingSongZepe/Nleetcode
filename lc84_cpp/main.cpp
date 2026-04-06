#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <stack>

using std::vector;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        std::stack<int> dec_stack;
        int ma
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    vector<int> heights = {2,1,5,6,2,3};
    int result;

    result = sol->largestRectangleArea(heights);
    std::cout << result << "\n";

    heights = {2, 4};
    result = sol->largestRectangleArea(heights);
    std::cout << result << "\n";


    return 0;
}

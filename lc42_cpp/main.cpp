#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

typedef long long LL;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

template <typename T>
void print_vector_ln(const vector<T>& v) {
    print_vector(v); std::cout << "\n";
}

template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

// leetcode tree node
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int l = 0, r = n-1;
        while (l < r && height[l] == 0) l++;
        while (l < r && height[r] == 0) r--;
        
        int stage = std::min(height[l], height[r]);
        int sum = (r-l+1) * stage;
        
        while (l < r) {
            if (height[l] <= height[r]) {
                int ll = l;
                while (ll < r && height[ll] <= height[l]) {
                    sum -= height[ll];
                    ll++;
                } l = ll;
            } else {
                int rr = r;
                while (l < rr && height[rr] <= height[r]) {
                    sum -= height[rr];
                    rr--;
                } r = rr;
            }
            // add new level
            int new_stage = std::min(height[l], height[r]);
            sum += (r-l+1) * (new_stage - stage);
            stage = new_stage;
        }

        return sum - stage;
    }
};


int main()
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> height;
    height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    result = sol->trap(height);
    std::cout << result << std::endl;

    height = {4, 2, 0, 3, 2, 5};
    result = sol->trap(height);
    std::cout << result << std::endl;

    return 0;
}

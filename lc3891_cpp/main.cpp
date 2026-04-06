#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <limits>
#include <vector>

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
    typedef long long LL;
    struct State {
        int cnt;
        LL cost;
        State() = default;
        State(int cnt, LL cost) : cnt(cnt), cost(cost) {}
    };

    LL minIncrease(vector<int>& nums) {
        // dp[i][0] means the min operations to get full combo without taking current as a special index
        // dp[i][1]
        int n = nums.size();
        State dp[2]{};

        // return true if s1 is `better` than s2
        auto compare_state = [](const State& s1, const State& s2) {
            if (s1.cnt != s2.cnt) {
                return s1.cnt > s2.cnt;
            } return s1.cost < s2.cost;
        };
    
        for (int i = 1; i < n-1; i++) {
            State odp[2]{dp[0], dp[1]};

            LL take_cost = std::max(0, std::max(nums[i+1], nums[i-1]) - nums[i] + 1);
            if (compare_state(odp[0], odp[1])) {
                dp[0] = odp[0];
            } else {
                dp[0] = odp[1];
            }
            dp[1] = State(odp[0].cnt + 1, odp[0].cost + take_cost);
        }

        State& final_state = compare_state(dp[0], dp[1]) ? dp[0] : dp[1];
        return final_state.cost;
    }
};


int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> nums;

    nums = {1, 2, 2};
    result = sol->minIncrease(nums);
    std::cout << result << std::endl;

    nums = {2, 1, 1, 3};
    result = sol->minIncrease(nums);
    std::cout << result << std::endl;

    nums = {5, 2, 1, 4, 3};
    result = sol->minIncrease(nums);
    std::cout << result << std::endl;

    return 0;
}

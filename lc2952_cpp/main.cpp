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

#include <algorithm>
#include <unordered_set>
class Solution {
public:
    typedef long long LL;
    int minimumAddedCoins(vector<int>& coins, int target) {
        std::sort(coins.begin(), coins.end());

        LL reach = 0;
        int i = 0;
        int n = coins.size();
        int n_coin = 0;

        while (reach < target) {
            if (i < n && coins[i] <= reach + 1) {
                reach += coins[i];
                i++;
            } else { 
                reach += reach + 1;
                n_coin++;
            }
        }

        return n_coin;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> coins;
    int target;

    coins = {1, 4, 10};
    target = 19;
    result = sol->minimumAddedCoins(coins, target);
    std::cout << result << std::endl;

    coins = {1, 4, 10, 5, 7, 19};
    target = 19;
    result = sol->minimumAddedCoins(coins, target);
    std::cout << result << std::endl;


    return 0;
}

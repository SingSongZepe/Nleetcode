#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <limits>
#include <vector>

using std::vector;
using std::array;
using std::string;

class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size();
        int n = coins[0].size();
        const int INF = 1e9;
        vector<vector<array<int, 3>>> dp(m+1, vector<array<int, 3>>(n+1, {-INF, -INF, -INF}));
        dp[0][1][0] = 0;
        dp[1][0][0] = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (coins[i][j] >= 0) {
                    for (int k = 0; k < 3; k++) {
                        dp[i+1][j+1][k] = std::max(dp[i+1][j][k], dp[i][j+1][k]) + coins[i][j];
                    }
                } else {
                    // k = 1, 2
                    for (int k = 1; k < 3; k++) {
                        // use neutralization
                        dp[i+1][j+1][k] = std::max(dp[i+1][j][k-1], dp[i][j+1][k-1]);
                        // don't use neutrailization
                        dp[i+1][j+1][k] = std::max(dp[i+1][j+1][k], std::max(dp[i+1][j][k], dp[i][j+1][k]) + coins[i][j]);
                    }
                    // k = 0 and don't use neut.
                    dp[i+1][j+1][0] = std::max(dp[i+1][j][0], dp[i][j+1][0]) + coins[i][j];
                }
            }
        }
        
        return std::max(dp[m][n][2], std::max(dp[m][n][1], dp[m][n][0]));
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;
    vector<vector<int>> coins;
    
    coins = {{0,1,-1},{1,-2,3},{2,-3,4}};
    result = sol->maximumAmount(coins);
    std::cout << result << std::endl;

    coins = {{10, 10, 10}, {10, 10, 10}};
    result = sol->maximumAmount(coins);
    std::cout << result << std::endl;
    
    return 0;
}

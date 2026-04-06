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

class Solution {
public:
    typedef long long LL;
    const int MOD = 1e9 + 7;
    int dieSimulator(int n, vector<int>& rollMax) {
        
        // dp[i][j]
        vector<vector<LL>> dp(6, vector<LL>(16, 0));
        for (int j = 0; j < 6; j++) {
            dp[j][1] = 1;
        }

        for (int i = 2; i <= n; i++) { // i represent roll time
            LL valid_comb = 0;
            for (int j = 0; j < 6; j++) {
                for (int k = 1; k <= rollMax[j]; k++) {
                    valid_comb = (valid_comb + dp[j][k]) % MOD;
                }
            }

            vector<vector<LL>> ndp(6, vector<LL>(16, 0));
            // 
            for (int j = 0; j < 6; j++) {
                LL prev_is_j = 0;
                for (int k = 1; k <= rollMax[j]; k++) {
                    prev_is_j = (prev_is_j + dp[j][k]) % MOD;                    
                }
                ndp[j][1] = (valid_comb - prev_is_j + MOD) % MOD; 

                // 
                for (int k = 2; k <= rollMax[j]; k++) {
                    ndp[j][k] = dp[j][k-1];
                }
            }
            dp = std::move(ndp);
        }
        
        LL res = 0;
        for (int j = 0; j < 6; j++) {
            for (int k = 1; k <= rollMax[j]; k++) {
                res = (res + dp[j][k]) % MOD;
            }
        }
        return res;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    vector<int> rollMax;
    int result;

    n = 2;
    rollMax = {1, 1, 2, 2, 3, 3};
    result = sol->dieSimulator(n, rollMax);
    std::cout << result << std::endl;

    n = 2;
    rollMax = {1, 1, 1, 1, 1, 1};
    result = sol->dieSimulator(n, rollMax);
    std::cout << result << std::endl;

    return 0;
}

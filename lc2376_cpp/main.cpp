#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;
using std::max;
using std::min;

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

// counts[0] means number of special numbers in range 1-9
// count [1] range 1-99
// count [1] range 1-999
// int counts[10];
// bool f = []() {
//     counts[0] = 9;
//     counts[1] = counts[0] + 9 * 9;
//     counts[2] = counts[1] + 9 * 9 * 8;
//     counts[3] = counts[2] + 9 * 9 * 8 * 7;
//     counts[4] = counts[3] + 9 * 9 * 8 * 7 * 6;
//     counts[5] = counts[4] + 9 * 9 * 8 * 7 * 6 * 5;
//     counts[6] = counts[5] + 9 * 9 * 8 * 7 * 6 * 5 * 4;
//     counts[7] = counts[6] + 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3;
//     counts[8] = counts[7] + 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2;
//     counts[9] = counts[8] + 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1;
//     return true;
// } ();

// #include <cmath>
// class Solution {
// public:
//     int countSpecialNumbers(int n) {
//         int tot = 0;
//         for (int x = 9; x > 0; x--) {
//             if (n > (int)std::pow(10, x)) {
//                 tot += counts[x-1];
//                 break;
//             }
//         }
//         std::cout << "tot: " << tot << std::endl;
//         // dp[i][j] means the number of special number if right-first i-th digit selects j
//         // 215
//         // dp[0][0] = 0
//         // dp[1][1] = sum(dp[0][0], dp[0][1], dp[])
//         vector<vector<int>> dp(10, vector<int>(10, 0));
//         // the right-first digit
//         int variant = n % 10;
//         for (int j = (n < 10 ? 1 : 0); j <= variant; j++) {
//             dp[0][j] = 1; 
//         }
//         n /= 10;
//         std::cout << "n: " << n << std::endl;

//         int i = 0;
//         for (i = 1; i < 10 && n > 0; i++) {
//             int variant = i % 10;
//             for (int j = (n < 10 ? 1 : 0); j <= variant; j++) {
//                 for (int k = 0; k < 10; k++) if (j != k) dp[i][j] += dp[i-1][k];
//             }
//             n /= 10;
//             std::cout << "n: " << n << std::endl;
//         }

//         for (int j = 1; j < 10; j++) {
//             tot += dp[i][j];
//         }
//         std::cout << "tot: " << tot << std::endl;
        
//         return tot;
//     }
// };


class Solution {
public:
    int memo[11][1 << 10];
    string s;
    int dfs(int i, int mask, bool is_less, bool is_started) {
        if (i == s.size()) return is_started;
        if (is_less && is_started && memo[i][mask] != -1) return memo[i][mask];

        int limit = is_less ? 9 : s[i] - '0';

        int res = 0;
        for (int d = 0; d <= limit; d++) {
            if (!is_started && !d) { // leading zero
                res += dfs(i+1, mask, true, false);
            } else if (!(mask & (1 << d))) {
                res += dfs(i+1, mask | (1 << d), is_less || (d < limit), true);
            }
        }
        if (is_less && is_started) memo[i][mask] = res;
        
        return res;
    }
    int countSpecialNumbers(int n) {
        s = std::to_string(n);
        memset(memo, -1, sizeof(memo));
        return dfs(0, 0, false, false);
    }
};

// more efficient
// math combination
typedef uint32_t uint;
using namespace std;
class Solution1 {
public:
    int countSpecialNumbers(int n) {
        const auto digits = to_string(n);
        const int len = digits.size();
        
        const auto frac = [] (int n) {
            long long ret = 1;
            for (int i = 1; i <= n; i++) ret *= i;
            return ret;
        };

        int ans = 0;
        for (uint i = 0; i < (1 << 10); i++) {
            const int cnt = __builtin_popcount(i);
            if (cnt > len) continue;
            if (cnt < len) {
                ans += frac(cnt);
                if ((i >> 0) & 1) ans -= frac(cnt - 1);
                continue;
            }
        }

        for (uint i = 0, used = 0; i <= len; i++) {
            if (i == len) {
                ans++;
                break;
            }
            const uint cur_digit = digits[i] - '0';
            for (int j = (i == 0 ? 1 : 0); j < cur_digit; j++) {
                if (used >> j & 1) continue;
                const int remaining_avail = 10 - __builtin_popcount(used) - 1;
                const int needed = len - i - 1;
                ans += frac(remaining_avail) / frac(remaining_avail - needed);
            }
            if ((used >> cur_digit) & 1) break;
            used |= 1 << cur_digit;
        }
        return ans - 1; // subtract "0"
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    n = 20;
    result = sol->countSpecialNumbers(n);
    std::cout << result << std::endl;

    n = 5;
    result = sol->countSpecialNumbers(n);
    std::cout << result << std::endl;


    return 0;
}

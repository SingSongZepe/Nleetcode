#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <limits>

using std::vector;
using std::string;

typedef long long LL;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

// #define DBUG

class Solution {
public:
    typedef long long LL;
    const LL INF = 1e16;
    int minOperations(vector<int>& nums, int k) {
        if (k == 0) return 0;
        int n = nums.size();
        if (n / 2 < k) return -1; // impossible
        
        vector<LL> cost(n);
        for(int i = 0; i < n; i++) {
            int prev = (i - 1 + n) % n;
            int next = (i + 1) % n;
            cost[i] = std::max(0LL, (LL) std::max(nums[prev], nums[next]) + 1 - nums[i]);
        }

        LL min_ops = INF;
        { 
            // case 1
            // when the first one is a peak
            // dp[i][j] means the minimum operations for first i elems to make j peak
            vector<vector<std::array<LL, 2>>> dp(n, vector<std::array<LL, 2>>(k + 1, {INF, INF}));
            dp[0][1][1] = cost[0];
            // for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i < n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);
                    // if take current one
                    if (i > 1 && dp[i-1][j-1][0] < INF) {
                        dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            // 
            min_ops = std::min(min_ops, std::min(dp[n-2][k][0], dp[n-2][k][1]));
#ifdef DBUG
            std::cout << "first elem is a peak\n";
            std::cout << std::min(dp[n-2][k][0], dp[n-2][k][1]) << std::endl;
#endif
        }

        {
            // case 2
            // when the last one is a peak
            vector<vector<std::array<LL, 2>>> dp(n, vector<std::array<LL, 2>>(k + 1, {INF, INF}));
            dp[0][0][0] = 0;
            for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i <= n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take the current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);

                    if (dp[i-1][j-1][0] != INF) {
                        if (i != n-2) dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            min_ops = std::min(min_ops, dp[n-1][k][1]);
#ifdef DBUG
            std::cout << "last elem is a peak\n";
            std::cout << std::min(min_ops, dp[n-1][k][1]) << std::endl;
#endif
        }
        
        {
            //case 3
            // when the neither first nor last one is a peak
            vector<vector<std::array<LL, 2>>> dp(n, vector<std::array<LL, 2>>(k + 1, {INF, INF}));
            dp[0][0][0] = 0; 
            for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i < n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);
                    // if take current one
                    if (dp[i-1][j-1][0] < INF) {
                        dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            // 
            min_ops = std::min(min_ops, std::min(dp[n-2][k][0], dp[n-2][k][1]));
#ifdef DBUG
            std::cout << "neither the first nor the last elem is a peak\n";
            std::cout << std::min(dp[n-1][k][0], dp[n-1][k][1]) << std::endl;
#endif
        }

        return min_ops;
    }
};

// use int 
class Solution1 {
public:
    const int INF = 1e9;
    int minOperations(vector<int>& nums, int k) {
        if (k == 0) return 0;
        int n = nums.size();
        if (n / 2 < k) return -1; // impossible
        
        vector<int> cost(n);
        for(int i = 0; i < n; i++) {
            int prev = (i - 1 + n) % n;
            int next = (i + 1) % n;
            cost[i] = std::max(0, std::max(nums[prev], nums[next]) + 1 - nums[i]);
        }

        int min_ops = INF;
        { 
            // case 1
            // when the first one is a peak
            // dp[i][j] means the minimum operations for first i elems to make j peak
            vector<vector<std::array<int, 2>>> dp(n, vector<std::array<int, 2>>(k + 1, {INF, INF}));
            dp[0][1][1] = cost[0];
            // for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i < n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);
                    // if take current one
                    if (i > 1 && dp[i-1][j-1][0] < INF) {
                        dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            // 
            min_ops = std::min(min_ops, std::min(dp[n-2][k][0], dp[n-2][k][1]));
#ifdef DBUG
            std::cout << "first elem is a peak\n";
            std::cout << std::min(dp[n-2][k][0], dp[n-2][k][1]) << std::endl;
#endif
        }

        {
            // case 2
            // when the last one is a peak
            vector<vector<std::array<int, 2>>> dp(n, vector<std::array<int, 2>>(k + 1, {INF, INF}));
            dp[0][0][0] = 0;
            for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i <= n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take the current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);

                    if (dp[i-1][j-1][0] != INF) {
                        if (i != n-2) dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            min_ops = std::min(min_ops, dp[n-1][k][1]);
#ifdef DBUG
            std::cout << "last elem is a peak\n";
            std::cout << std::min(min_ops, dp[n-1][k][1]) << std::endl;
#endif
        }
        
        {
            //case 3
            // when the neither first nor last one is a peak
            vector<vector<std::array<int, 2>>> dp(n, vector<std::array<int, 2>>(k + 1, {INF, INF}));
            dp[0][0][0] = 0; 
            for (int i = 0; i < n; i++) dp[i][0][0] = 0; // no peaks, no operations
            for (int i = 1; i < n-1; i++) {
                for (int j = 1; j <= k; j++) {
                    // if don't take current one
                    dp[i][j][0] = std::min(dp[i-1][j][0], dp[i-1][j][1]);
                    // if take current one
                    if (dp[i-1][j-1][0] < INF) {
                        dp[i][j][1] = dp[i-1][j-1][0] + cost[i];
                    }
                }
            }
            // 
            min_ops = std::min(min_ops, std::min(dp[n-2][k][0], dp[n-2][k][1]));
#ifdef DBUG
            std::cout << "neither the first nor the last elem is a peak\n";
            std::cout << std::min(dp[n-1][k][0], dp[n-1][k][1]) << std::endl;
#endif
        }

        return min_ops;
    }
};


#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    long long val;
    int l, r;
    bool exists = true;
};

// best algo
// WQS regret greedy 
class Solution2 {
public:
    long long solveGreedy(int n, int k, const vector<long long>& initial_costs) {
        if (k <= 0) return 0;
        if (k > n / 2) return -1;

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        vector<Node> nodes(n);

        for (int i = 0; i < n; ++i) {
            nodes[i] = {initial_costs[i], (i - 1 + n) % n, (i + 1) % n};
            pq.push({initial_costs[i], i});
        }

        long long total_cost = 0;
        for (int i = 0; i < k; ++i) {
            while (!pq.empty() && !nodes[pq.top().second].exists) {
                pq.pop();
            }
            
            auto [val, idx] = pq.top();
            pq.pop();

            total_cost += val;

            // Regret logic: New cost = cost[L] + cost[R] - cost[curr]
            int L = nodes[idx].l;
            int R = nodes[idx].r;
            
            nodes[idx].val = nodes[L].val + nodes[R].val - nodes[idx].val;
            
            // Remove neighbors
            nodes[L].exists = false;
            nodes[R].exists = false;
            
            // Relink the doubly linked list
            int LL = nodes[L].l;
            int RR = nodes[R].r;
            nodes[idx].l = LL;
            nodes[idx].r = RR;
            nodes[LL].r = idx;
            nodes[RR].l = idx;

            pq.push({nodes[idx].val, idx});
        }

        return total_cost;
    }

    long long minOperations(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 0) return 0;
        if (k > n / 2) return -1;

        vector<long long> costs(n);
        for (int i = 0; i < n; ++i) {
            long long left = nums[(i - 1 + n) % n];
            long long right = nums[(i + 1) % n];
            costs[i] = max(0LL, max(left, right) + 1 - (long long)nums[i]);
        }

        return solveGreedy(n, k, costs);
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> nums;
    int k;

    nums = {2,1,2};
    k = 1;
    result = sol->minOperations(nums, k);
    std::cout << result << std::endl;

    nums = {4, 5, 3, 6};
    k = 2;
    result = sol->minOperations(nums, k);
    std::cout << result << std::endl;

    nums = {3, 7, 3};
    k = 2;
    result = sol->minOperations(nums, k);
    std::cout << result << std::endl;

    nums = {-8, 11, -13};
    k = 1;
    result = sol->minOperations(nums, k);
    std::cout << result << std::endl;

    return 0;
}

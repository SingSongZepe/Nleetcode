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

std::ostream& operator<<(std::ostream& os, const std::pair<int, int>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}


#include <algorithm>
class Solution {
public:
    template <typename T1, typename T2>
    vector<std::pair<T1, T2>> zip(vector<T1>& v1, vector<T2>& v2) {
        // we should acknowledge that v1.size() <= v2.size()
        size_t n = std::min(v1.size(), v2.size());

        vector<std::pair<T1, T2>> zv;
        zv.reserve(n);

        for (int i = 0; i < n; i++) {
            zv.emplace_back(std::move(v1[i]), std::move(v2[i]));
        }
        return zv;
    }

    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        vector<std::pair<int, int>> pos_dis = zip(robots, distance);
        std::sort(pos_dis.begin(), pos_dis.end(), [](const std::pair<int, int>& a, const std::pair<int, int>&b) {
            return a.first < b.first;
        });
        // take data into cache
        // for (int i = 0; i < walls.size(); i += 16) {
        //     __builtin_prefetch(&walls[i], 0, 3);
        // }
        std::sort(walls.begin(), walls.end());

        int n = pos_dis.size();
        vector<int> leftrange(n, 0);
        vector<int> rightrange(n, 0);
        vector<int> intersection(n-1, 0);

        // fill in the 3 vec
        for (int i = 0; i < n; i++) {
            // robot i left shooting bound
            int l = pos_dis[i].first - pos_dis[i].second;
            if (i > 0) {
                l = std::max(pos_dis[i-1].first+1, l); // can't override the pos of prev robot i-1
            }
            // robot i position;
            int p = pos_dis[i].first;
            // robot i right shooting bound
            int r = pos_dis[i].first + pos_dis[i].second;
            if (i < n-1) {
                r = std::min(pos_dis[i+1].first-1, r); // can't override the pos of next robot i+1
            }
            
            // fill leftrange, the number of walls falls in [l, p]
            auto l_it = std::lower_bound(walls.begin(), walls.end(), l);
            auto pu_it = std::upper_bound(walls.begin(), walls.end(), p);
            leftrange[i] = std::distance(l_it, pu_it);

            auto pl_it = std::lower_bound(walls.begin(), walls.end(), p);
            auto r_it = std::upper_bound(walls.begin(), walls.end(), r);
            rightrange[i] = std::distance(pl_it, r_it);
            
            // intersection part
            if (i < n-1) {
                // the left shooting bound of robot i+1
                int l = pos_dis[i+1].first - pos_dis[i+1].second;
                l = std::max(pos_dis[i].first+1, l);
                if (l > r) continue;

                auto l_it = std::lower_bound(walls.begin(), walls.end(), l);
                auto r_it = std::upper_bound(walls.begin(), walls.end(), r);
                intersection[i] = std::distance(l_it, r_it);
            }
        }

        // dp[i][0] means max walls prevous i robots can destroy and last one shoot left
        // dp[i][1] means max walls prevous i robots cans destroy and last one shoot right
        vector<std::array<int, 2>> dp(n, {0, 0});
        dp[0][0] = leftrange[0];
        dp[0][1] = rightrange[0];
        for (int i = 1; i < n; i++) {
            // the curr shoot left
            dp[i][0] = std::max(dp[i-1][0], dp[i-1][1] - intersection[i-1]) + leftrange[i];
            // the curr shoot right
            dp[i][1] = std::max(dp[i-1][0], dp[i-1][1]) + rightrange[i];
        }

        return std::max(dp[n-1][0], dp[n-1][1]);
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    vector<int> robots;
    vector<int> distance;
    vector<int> walls;

    robots = {10, 2};
    distance = {5, 1};
    walls = {5, 2, 7};
    result = sol->maxWalls(robots, distance, walls);
    std::cout << result << std::endl;

    return 0;
}

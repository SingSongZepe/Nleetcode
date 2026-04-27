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

#define id(r, c) (r*n+c)
#include <algorithm>
#include <unordered_map>
class Solution {
public:
    const int dr[4] = {0, 1, 0, -1};
    const int dc[4] = {1, 0, -1, 0};
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        // false means 
        // true means guard/wall/pos can be seen
        vector<bool> position(m*n, false);
        std::unordered_map<int, vector<int>> r_to_cs;
        std::unordered_map<int, vector<int>> c_to_rs;
        for (const auto& w : walls) {
            int r = w[0], c = w[1];
            position[id(r, c)] = true;
            r_to_cs[r].emplace_back(c);
            c_to_rs[r].emplace_back(r);
        }
        for (const auto& g : guards) {
            int r = g[0], c = g[1];
            position[id(r, c)] = true;
            r_to_cs[r].emplace_back(c);
            c_to_rs[r].emplace_back(r);
        }
        for (auto& [r, cs] : r_to_cs) std::sort(cs.begin(), cs.end());
        for (auto& [c, rs] : c_to_rs) std::sort(rs.begin(), rs.end());

        for (const auto& g : guards) {
            int r = g[0], c = g[1];

            
            // rightmost
            auto& cs = r_to_cs[r];
            for (int i = 0; i < cs.size(); i++) {
                // if ()
            }

            // leftmost

            // topmost

            //bottommost

        }
    }
};

class Solution1 {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<int> grid(m * n, 0);

        for (const auto& w : walls) grid[w[0] * n + w[1]] = 2;
        for (const auto& g : guards) grid[g[0] * n + g[1]] = 1;

        int dr[] = {0, 1, 0, -1};
        int dc[] = {1, 0, -1, 0};

        for (const auto& g : guards) {
            for (int i = 0; i < 4; ++i) {
                int r = g[0] + dr[i];
                int c = g[1] + dc[i];

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    int pos = r * n + c;
                    if (grid[pos] == 1 || grid[pos] == 2) break;
                    
                    grid[pos] = 3;
                    r += dr[i];
                    c += dc[i];
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m * n; ++i) {
            if (grid[i] == 0) count++;
        }

        return count;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

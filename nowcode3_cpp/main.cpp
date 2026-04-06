#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <string>
#include <functional>
#include <limits>

using std::vector;
using std::string;

class Solution {
public:
    int climb(vector<vector<int> >& grid, int step) {
        // write code here
        int n = grid.size();
        int m = grid[0].size();

        // (i, j) is accessable
        std::function<bool(int, int)> is_safe = [=](int i, int j) {
            if (i >= 0 && j >= 0 && i < n && j < m) {
                return true;
            } return false;
        };

        // find the min anx max pos
        int min_height = std::numeric_limits<int>::max();
        int max_height = 0;
        int min_i, min_j;
        int max_i, max_j;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] > max_height) {
                    max_height = grid[i][j];
                    max_i = i; max_j = j;
                }
                if (grid[i][j] < min_height) {
                    min_height = grid[i][j];
                    min_i = i; min_j = j;
                }
            }
        }

        int res = 0;
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        // dfs start with (i, j) to get to (max_i, max_j)
        std::function<void(int, int)> dfs = [&](int i, int j) {
            if (i == max_i && j == max_j) {
                res++;
                return;
            }
            for (int k = 0; k < 4; k++) {
                int ni = i + dx[k]; int nj = j + dy[k];
                if (is_safe(ni, nj)) {
                    int curr_height = grid[i][j];
                    int target_height = grid[ni][nj];
                    if (target_height > curr_height && target_height - curr_height <= step) { // new position
                        dfs(ni, nj);
                    }
                }
            }
        };

        dfs(min_i, min_j);

        return res;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    vector<vector<int>> grid = {{4, 3},{3, 2}};
    int step = 1;
    result = sol->climb(grid, step);
    std::cout << result << std::endl;

    return 0;
}

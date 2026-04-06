#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <string>
#include <functional>
#include <queue>

using std::vector;
using std::string;

class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        std::queue<std::pair<int, int>> q;
        bool found = false;

        std::function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || c < 0 || r >= n || c >= n || grid[r][c] != 1) return;
            grid[r][c] = 2; 
            q.push({r, c});
            dfs(r + 1, c); dfs(r - 1, c);
            dfs(r, c + 1); dfs(r, c - 1);
        };

        for (int i = 0; i < n && !found; i++) {
            for (int j = 0; j < n && !found; j++) {
                if (grid[i][j] == 1) {
                    dfs(i, j); 
                    found = true;
                }
            }
        }

        int steps = 0;
        int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
        
        while (!q.empty()) {
            int size = q.size();
            while (size--) {
                auto [r, c] = q.front(); q.pop();
                for (int i = 0; i < 4; i++) {
                    int nr = r + dx[i], nc = c + dy[i];
                    if (nr >= 0 && nc >= 0 && nr < n && nc < n) {
                        if (grid[nr][nc] == 1) return steps; 
                        if (grid[nr][nc] == 0) {
                            grid[nr][nc] = 2;
                            q.push({nr, nc});
                        }
                    }
                }
            }
            steps++;
        }
        return steps;
    }
};

// better
// from edge point
class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        std::queue<std::pair<int, int>> q;
        int dx[4] = {0, 0, 1, -1};
        int dy[4] = {1, -1, 0, 0};

        std::function<void(int, int)> dfs = [&](int r, int c) {
            grid[r][c] = 2; 
            bool isEdge = false;

            for (int i = 0; i < 4; i++) {
                int nr = r + dx[i], nc = c + dy[i];
                if (nr >= 0 && nc >= 0 && nr < n && nc < n) {
                    if (grid[nr][nc] == 0) isEdge = true; 
                    else if (grid[nr][nc] == 1) dfs(nr, nc); 
                }
            }
            
            if (isEdge) q.push({r, c}); 
        };

        bool found = false;
        for (int i = 0; i < n && !found; i++) {
            for (int j = 0; j < n && !found; j++) {
                if (grid[i][j] == 1) {
                    dfs(i, j);
                    found = true;
                }
            }
        }

        int steps = 0;
        while (!q.empty()) {
            int size = q.size();
            while (size--) {
                auto [r, c] = q.front(); q.pop();
                for (int i = 0; i < 4; i++) {
                    int nr = r + dx[i], nc = c + dy[i];
                    if (nr >= 0 && nc >= 0 && nr < n && nc < n) {
                        if (grid[nr][nc] == 1) return steps; 
                        if (grid[nr][nc] == 0) {
                            grid[nr][nc] = 2;
                            q.push({nr, nc});
                        }
                    }
                }
            }
            steps++;
        }
        return steps;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    vector<vector<int>> grid = {{0, 1}, {1, 0}};
    result = sol->shortestBridge(grid);
    std::cout << result << std::endl;

    return 0;
}

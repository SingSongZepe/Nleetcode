#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <functional>

using std::vector;

// this is implemented by dfs200209
// but bfs better
#define N 305

class Solution {
public:
    bool visited[N][N];
    int numIslands(vector<vector<char>>& grid) {
        memset(visited, 0x00, sizeof(visited));

        int m = grid.size();
        int n = grid[0].size();

        int component = 0;

        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        std::function<void(int, int)> dfs = [&](int i, int j) {
            visited[i][j] = true;
            for (int k = 0; k < 4; k++) {
                int ni = i + dx[k], nj = j + dy[k];
                if (ni >= 0 && nj >= 0 && ni < m && nj < n && !visited[ni][nj] && grid[ni][nj] == '1')
                    dfs(ni, nj);
            }
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    dfs(i, j);
                    component++;
                }
            }
        }
        
        return component;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;


    return 0;
}

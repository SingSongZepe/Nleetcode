#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

#define N 205

class Solution {
public:
    int uf[N];
    int find(int i) {
        return uf[i] == i ? i : uf[i] = find(uf[i]);
    }
    void merge(int i, int j) {
        int x = find(i);
        int y = find(j);

        uf[y] = x;
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        for (int i = 0; i < N; i++) uf[i] = i;

        int n = isConnected.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (isConnected[i][j]) merge(i, j);
            }
        }

        int component = 0;
        for (int i = 0; i < n; i++) {
            if (find(i) == i) component++;
        }

        return component;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int result;
    vector<vector<int>> isConnected = {{1,1,0},{1,1,0},{0,0,1}};
    
    result = sol->findCircleNum(isConnected);
    std::cout << result << std::endl;


    return 0;
}

#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <queue>

using std::vector;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ind(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        for (const auto& prereq : prerequisites) {
            int a = prereq[0]; int b = prereq[1];
            ind[a]++;
            adj[b].emplace_back(a); 
        }

        std::queue<int> q;
        for (int i = 0; i < numCourses; i++){
            if (!ind[i]) {
                q.emplace(i); // root
            }
        } 
        
        vector<int> recommended;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            recommended.emplace_back(u);
            for (int v : adj[u]) {
                ind[v]--;
                if (!ind[v]) {
                    q.emplace(v);
                }
            }
        }
        
        if (recommended.size() != numCourses) return {};

        return recommended;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;



    return 0;
}

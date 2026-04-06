#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using std::string;
using std::vector;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        std::unordered_set<string> dict(wordDict.begin(), wordDict.end());
        std::queue<int> q;
        q.emplace(0); // [l, r)

        int len = s.size();
        vector<bool> visited(len + 1, false);

        while (!q.empty()) {
            int l = q.front(); q.pop();
            if (l == len) return true;
            for (int r = l+1; r <= len; r++) { // [l, r)
                if (!visited[r] && dict.count(s.substr(l, r - l))) {
                    // cut [l, r)
                    // [r, ) left
                    q.emplace(r);
                    visited[r] = true;
                }
            }
        }

        return false;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    string n;
    vector<string> wordDict;
    int result;

    n = "applepenapple";
    wordDict = {
        "apple", "pen"
    };
    result = sol->wordBreak(n, wordDict);
    std::cout << result << std::endl;

    


    return 0;
}

#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <string>
#include <functional>
#include <algorithm>

using std::vector;
using std::string;

#define N 14005
#define id(x) x - 'a'
class Solution {
public:
    int trie[N][26];
    int idx;
    void insert(string& s) {
        reverse(s.begin(), s.end());

        int curr = 0;
        for (char c : s) {
            if (!trie[curr][id(c)]) {
                trie[curr][id(c)] = ++idx;
            }
            curr = trie[curr][id(c)];
        }
    }
    int minimumLengthEncoding(vector<string>& words) {
        memset(trie, 0x00, sizeof(trie));
        idx = 0;

        for (auto& word : words) {
            insert(word);
        }

        // dfs traverse
        int total_len = 0;
        std::function<void(int, int)> dfs = [&](int i, int depth) {
            bool is_leaf = true;
            for (int j = 0; j < 26; j++) {
                if (trie[i][j]) {
                    is_leaf = false;
                    dfs(trie[i][j], depth + 1);
                }
            }
            if (is_leaf) {
                total_len += depth + 1;
            }
        };
        dfs(0, 0);

        return total_len;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    vector<string> v;
    int result;

    v = {"time", "me", "bell"};
    result = sol->minimumLengthEncoding(v);
    std::cout << result << std::endl;

    return 0;
}

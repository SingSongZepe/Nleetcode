#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <unordered_set>
#include <queue>

using std::vector;
using std::string;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_set<string> st(wordList.begin(), wordList.end());
        if (!st.count(endWord)) return 0; // target not included

        std::queue<string> q;
        q.emplace(beginWord);
        st.erase(beginWord);

        int step = 1;
        while (!q.empty()) {
            int size = q.size();
            
            for (int _ = 0; _ < size; _++) {
                auto word = q.front(); q.pop();
                for (int i = 0; i < beginWord.size(); i++) {
                    char originChar = word[i]; 

                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == originChar) continue;

                        word[i] = c;
                        if (word == endWord) return step + 1;
                        if (st.count(word))  {
                            q.emplace(word);
                            st.erase(word);
                        }
                    }
                    word[i] = originChar;
                }
            }
            step++;
        }
        
        return 0;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    string beginWold = "hit";
    string endWold = "cog";
    vector<string> dic = {
        "hot","dot","dog","lot","log","cog"
    };

    result = sol->ladderLength(beginWold, endWold, dic);
    std::cout << result << std::endl;

    return 0;
}

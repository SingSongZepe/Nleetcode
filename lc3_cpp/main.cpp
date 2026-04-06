#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <unordered_set>

using std::string;

// and a better algo is implemented by lastPos
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> st;

        int l = 0;
        int maxlen = 0;
        for (int r = 0; r < s.size(); r++) {
            while (l < r && st.count(s[r])) {
                st.erase(s[l]);
                l++;
            }
            st.emplace(s[r]);
            maxlen = std::max(maxlen, (int) st.size()); 
        }

        return maxlen;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;



    return 0;
}

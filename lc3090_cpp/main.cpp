#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <unordered_map>

using std::vector;
using std::string;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

#define id(c) ((c) - 'a')
class Solution {
public:
    int maximumLengthSubstring(string s) {
        // std::unordered_map<char, int8_t> mp;
        int8_t mp[26];
        memset(mp, 0x00, sizeof(mp));

        int l = 0;
        int maxLen = 0;
        for (int r = 0; r < s.size(); r++) {
            mp[id(s[r])]++;
            while (l < r && mp[id(s[r])] > 2) {
                mp[id(s[l++])]--;
            }
            maxLen = std::max(maxLen, r-l+1);
        }

        return maxLen;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    string s = "bcbbbcba";
    result = sol->maximumLengthSubstring(s);
    std::cout << result << std::endl;

    return 0;
}

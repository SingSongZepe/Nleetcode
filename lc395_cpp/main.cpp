#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

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
    int longestSubstring(string s, int k) {
        
        int counts[26]{};

        for (const char& c : s) {
            counts[id(c)]++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (counts[id(s[i])] < k) {
                int left_max = longestSubstring(s.substr(0, i), k);
                int j = i + 1;
                while (s[j] == s[i]) j++;
                int right_max = longestSubstring(s.substr(j), k);
                
                return std::max(left_max, right_max);
            }
        }
        
        return s.size();
    }
};


int main() 
{
    // string v = "jkljkl";
    // std::cout << v.substr(0, 3);
    // return 0;
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;
    string s;
    int k;

    s = "aaabb";
    k = 3;
    result = sol->longestSubstring(s, k);
    std::cout << result << std::endl;

    s = "ababbc";
    k = 2;
    result = sol->longestSubstring(s, k);
    std::cout << result << std::endl;

    return 0;
}

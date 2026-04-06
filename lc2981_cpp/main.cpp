#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <unordered_map>
#include <functional>

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
    // check whether mid is valid
    bool check(vector<int> counts[], int mid) {
        if (mid <= 0) return true;
        // iterate over all chars
        for (int i = 0; i < 26; i++) {
            int total = 0;
            for (const int cnt : counts[i]) {
                if (cnt >= mid)
                total += cnt - mid + 1;
            }
            if (total >= 3) {
                return true;
            }
        }
        
        return false;
    }
    int maximumLength(string s) {
        // count[i] means the continuous segment of char 'i'
        vector<int> counts[26];
        int n = s.size();

        int maxlen = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            int len = j - i;
            maxlen = std::max(len, maxlen);
            counts[id(s[i])].push_back(len);
            i = j;
        }

        // binary search
        int l = 0; int r = maxlen; // [l, r]
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(counts, mid)) { // valid
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        
        return l == 0 ? -1 : l;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;
    string s;

    s = "aaaa";
    result = sol->maximumLength(s);
    std::cout << result << std::endl;

    s = "abcdef";
    result = sol->maximumLength(s);
    std::cout << result << std::endl;

    s = "abcaba";
    result = sol->maximumLength(s);
    std::cout << result << std::endl;

    return 0;
}

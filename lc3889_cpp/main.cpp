#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using std::vector;
using std::string;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}


char mirror(char c) {
    if ('0' <= c && c <= '9') { // isdigit
        return '0' + '9' - c;
    } else { // is lowercase letter
        return 'a' + 'z' - c;
    }
}

class Solution {
public:
    int mirrorFrequency(string s) {
        std::unordered_map<char, int> mp;
        for (const char c : s) mp[c]++;

        int val = 0;
        std::unordered_set<char> processed;
        for (const auto& [c, freq] : mp) {
            if (processed.count(c)) continue;
            int mc = mirror(c);
            int mfreq = 0;
            if (mp.count(mc)) mfreq = mp.at(mc);
            val += std::abs(freq - mfreq);

            processed.emplace(c);
            processed.emplace(mc);
        }
        return val;
    }
};


class Solution1 {
public:
char mirror(char c) {
        if (c >= '0' && c <= '9') return '0' + '9' - c; // is digit
        return 'a' + 'z' - c;                           // is lowercase letter
    }
    int mirrorFrequency(string s) {
        int mp[128]{};
        for (const char c : s) mp[c]++;

        int val = 0;
        std::unordered_set<char> processed;
        for (char c = '0'; c <= '9'; c++) {
            int mc = mirror(c);
            val += std::abs(mp[c] - mp[mc]);
            mp[c] = 0; mp[mc] = 0;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            int mc = mirror(c);
            val += std::abs(mp[c] - mp[mc]);
            mp[c] = 0; mp[mc] = 0;
        }
        return val;
    }
};

void test() {
    for (char c = 'a'; c <= 'z'; c++) {
        std::cout << c << " " << mirror(c) << std::endl;
    }
}

int main() 
{
    test();
    return 0;
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

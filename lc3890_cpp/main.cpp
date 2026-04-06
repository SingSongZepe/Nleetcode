#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_map>

using std::vector;
using std::string;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    } std::cout << std::endl;
}

// class Solution {
// public:
//     int max_comp = 794; // 2 * 794 ** 3 > 1e9
//     vector<int> findGoodIntegers(int n) {
//         if (n < 1729) return {};
//         if (n < 4104) return {1729};
//         if (n == 4104) return {1729, 4104};

//         // main body
//         vector<int> res{1729, 4104};
//         for (int nn = 4105; nn < n; nn++) {
//             for (int i = 1; i < max_comp; i++) {
//                 int target = n - i*i*i;
//                 double cbrt_target = std::cbrt(target);
//                 if (cbrt_target != (int) cbrt_target) continue;
//                 int cbrtt = (int) cbrt_target;
//                 if (cbrtt*cbrtt*cbrtt == target) res.push_back(nn); 
//             }
//         }

//         return res;
//     }
// };

// sieve
#include <algorithm>
class Solution {
public:
    // typedef long long LL;
    int max_comp = 794; // 2 * 794 ** 3 > 1e9
    vector<int> findGoodIntegers(int n) {
        if (n < 1729) return {};
        if (n < 4104) return {1729};
        if (n == 4104) return {1729, 4104};

        std::unordered_map<int, uint8_t> cnt; 
        for (int i = 1; i < max_comp; i++) {
            for (int j = i; ; j++) {
                int x = i*i*i + j*j*j;
                if (x > n) break;
                cnt[x]++;
            }
        }

        vector<int> result;
        for (const auto& [x, freq] : cnt) {
            if (freq > 1) result.emplace_back(x);
        }
        std::sort(result.begin(), result.end());
        return result;
    }
};

#include <map>
#include <set>
// trick way
std::map<int, int> mp;
std::set<int> good;

bool f = []() {
    for(long long i = 1; i <= 1000; i++) {
        for(long long j = i; j <= 1000; j++) {
            mp[(i * i * i) + (j * j * j)]++;
        }
    }
    for(auto it : mp) {
        if(it.second > 1) {
            good.insert(it.first);
        }
    }
    return true;
} ();


class Solution {
public:
    vector<int> findGoodIntegers(int n) {
        vector<int> ans;
        for(int x : good) {
            if(x > n) break;
            ans.push_back(x);
        }
        return ans;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    auto sol1 = std::make_unique<Solution>();
    
    int n;
    vector<int> result;

    n = 4104;
    result = sol->findGoodIntegers(n);
    print_vector(result);

    n = 1e6;
    result = sol->findGoodIntegers(n);
    print_vector(result);


    n = 4104;
    result = sol1->findGoodIntegers(n);
    print_vector(result);

    n = 1e6;
    result = sol1->findGoodIntegers(n);
    print_vector(result);

    return 0;
}

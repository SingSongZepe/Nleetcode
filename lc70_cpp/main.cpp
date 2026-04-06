#include <iostream>
#include <memory>
#include <string.h>

class Solution {
public:
    int cache[50];
    int climbStairs(int n) {
        memset(cache, 0x00, sizeof(cache));
        return f(n);
    }
    int f(int n) {
        if (n < 2) return 1;
        if (cache[n] != 0) return cache[n];
        int res = f(n-1) + f(n-2);
        if (cache[n] == 0) cache[n] = res;
        return res;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    n = 2;
    result = sol->climbStairs(n);
    std::cout << result << std::endl;

    n = 3;
    result = sol->climbStairs(n);
    std::cout << result << std::endl;

    n = 45;
    result = sol->climbStairs(n);
    std::cout << result << std::endl;

    return 0;
}

#include <iostream>
#include <memory>
#include <string.h>


#define N 35

class Solution {
public:
    int fib(int n) {
        int fibs[N];
        memset(fibs, 0x00, sizeof(fibs));
        fibs[1] = 1;

        for (int i = 2; i <= n; i++) {
            fibs[i] = fibs[i-1] + fibs[i-2];
        }
        return fibs[n];
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    n = 2;
    result = sol->fib(n);
    std::cout << result << std::endl;

    n = 3;
    result = sol->fib(n);
    std::cout << result << std::endl;

    n = 4;
    result = sol->fib(n);
    std::cout << result << std::endl;

    return 0;
}

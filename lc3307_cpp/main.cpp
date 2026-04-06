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

class Solution {
public:
    typedef long long LL;
    char kthCharacter(LL k, vector<int>& operations) {
        
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    char result;

    int k;
    vector<int> operations;

    k = 5;
    operations = {0, 0, 0};
    result = sol->kthCharacter(k, operations);
    std::cout << result << std::endl;

    return 0;
}

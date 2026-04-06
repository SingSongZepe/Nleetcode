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
    bool judgeCircle(string moves) {
        int hori = 0, vert = 0;
        for (const char c : moves) {
            if (c == 'U') vert++;
            else if (c == 'D') vert--;
            else if (c == 'L') hori++;
            else hori--;
        }
        return !hori && !vert;
    }
};

class Solution1 {
public:
    const int H = 2e4+1;
    bool judgeCircle(string moves) {
        int dis = 0;
        for (const char c : moves) {
            if (c == 'U') dis++;
            else if (c == 'D') dis--;
            else if (c == 'L') dis -= H;
            else dis += H;
        }
        return !dis;
    }
};



int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    return 0;
}

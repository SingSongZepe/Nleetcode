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

#include <algorithm>
class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        std::sort(hBars.begin(), hBars.end());
        std::sort(vBars.begin(), vBars.end());

        // horizontal bar
        int hmax = 2;
        int hcurr = 2;
        for (int i = 1; i < hBars.size(); i++) {
            if (hBars[i] == hBars[i-1] + 1) { 
                hcurr++;
            } else {
                hmax = std::max(hmax, hcurr);
                hcurr = 2;
            }
        }
        hmax = std::max(hmax, hcurr);

        int vmax = 2;
        int vcurr = 2;
        for (int i = 1; i < vBars.size(); i++) {
            if (vBars[i] == vBars[i-1] + 1) { 
                vcurr++;
            } else {
                vmax = std::max(vmax, vcurr);
                vcurr = 2;
            }
        }
        vmax = std::max(vmax, vcurr);

        int edge_max = std::min(hmax, vmax);
        return edge_max * edge_max;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int m;
    vector<int> hBars;
    vector<int> vBars;
    int result;

    n = 2;
    m = 1;
    hBars = {2, 3};
    vBars = {2};
    result = sol->maximizeSquareHoleArea(n, m, hBars, vBars);
    std::cout << result << std::endl;

    n = 4;
    m = 40;
    hBars = {5, 3, 2, 4};
    vBars = {36, 41, 6, 34, 33};
    result = sol->maximizeSquareHoleArea(n, m, hBars, vBars);
    std::cout << result << std::endl;

    return 0;
}

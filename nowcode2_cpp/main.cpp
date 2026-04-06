#include <iostream>
#include <memory>
#include <string.h>
#include <unordered_set>
#include <limits>

#define NN 1005
class Solution {
public:
    int calculateSequence(int M, int N) {
        // write code here
        if (N <= M) return N;

        int nums[NN];
        for (int i = 1; i <= M; i++) {
            nums[i] = i;
        }
        // after M, from M+1
        for (int i = M+1; i <= N; i++) {
            int mx = 0;
            int mi = std::numeric_limits<int>::max();
            std::unordered_set<int> st;

            bool same_exist = false;
            for (int j = 0; j < M; j++) {
                
                int curr_num = nums[i-j-1];
                if (st.count(curr_num)) {
                    same_exist = true;
                }
                mx = std::max(mx, curr_num);
                mi = std::min(mi, curr_num);
                st.insert(curr_num);
            }
            if (same_exist) {
                nums[i] = mx + mi;
            } else {
                nums[i] = mx - mi;
            }
        }

        return nums[N];
    }
};


int main() 
{
    int M; int N;
    M = 5;
    N = 9;

    auto sol = std::make_unique<Solution>();
    int result;
    result = sol->calculateSequence(M, N);
    std::cout << result << std::endl; 

    return 0;
}

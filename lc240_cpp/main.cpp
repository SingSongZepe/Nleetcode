#include <iostream>
#include <memory>
#include <string.h>
#include <vector>

using std::vector;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();      // rows
        int n = matrix[0].size();   // columns

        // search in each row
        // bisearch horizontally
        // [l, r)
        for (int i = 0; i < m; i++) {
            const auto& row = matrix[i];

            int l = 0; int r = n;
            while (l < r) {
                int mid = (l + r) / 2; 

                if (row[mid] == target) return true;
                else if (row[mid] < target) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
        }
        return false;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    bool result;

    vector<vector<int>> matrix = {{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
    int target = 5;
    result = sol->searchMatrix(matrix, target);
    std::cout << result << std::endl; 

    matrix = {{-1, 3}};
    target = 3;
    result = sol->searchMatrix(matrix, target);
    std::cout << result << std::endl; 

    return 0;
}

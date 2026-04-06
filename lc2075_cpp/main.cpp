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
    string decodeCiphertext(string encodedText, int rows) {
        string result;
        int n = encodedText.size();
        result.reserve(n);
        int cols = n / rows;

        auto id = [=](int c, int r) {
            return r * cols + c + r;
        };
        for (int c = 0; ; c++) {
            for (int r = 0; r < rows; r++) {
                int i = id(c, r);
                if (i >= n) {
                    while (!result.empty() && result.back() == ' ') {
                        result.pop_back();
                    }
                    result.shrink_to_fit();
                    return result;
                } 
                result.push_back(encodedText[i]);
            }
        }

        throw std::runtime_error("unreachable!");
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    string result;

    string encodedText;
    int rows;

    encodedText = "ch   ie   pr";
    rows = 3;
    result = sol->decodeCiphertext(encodedText, rows);
    std::cout << result << std::endl;

    encodedText = "iveo    eed   l te   olc";
    rows = 4;
    result = sol->decodeCiphertext(encodedText, rows);
    std::cout << result << std::endl;

    return 0;
}

#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;

typedef long long LL;

template <typename T>
void print_vector(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    }
}

template <typename T>
void print_vector_ln(const vector<T>& v) {
    print_vector(v); std::cout << "\n";
}

template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

// leetcode tree node
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Robot {
private:
    int width;
    int height;
    int x = 0, y = 0;
    int dir = 0;        // east
    int circle_len;
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    bool moved = false;
    const string str_dirs[4] = {"East", "North", "West", "South"};
public:
    Robot(int width, int height) : width(width), height(height), circle_len(2*(width+height)-4) { }
    
    void step(int num) {
        moved = true;
        num %= circle_len;
        if (num == 0) num = circle_len;

        while (num) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx >= width ||     // right bound
                nx < 0 ||          // left bound
                ny >= height ||    // top bound
                ny < 0             // bottom bound
            ) { 
                dir = (dir + 1) % 4;
                continue;
            }
            x = nx;
            y = ny;
            num--;
        }
    }
    
    vector<int> getPos() {
        return {x, y};
    }
    
    string getDir() {
        if (x == 0 && y == 0 && !moved) return str_dirs[0];
        return str_dirs[dir];
    }
};


// Your Robot object will be instantiated and called as such:



int main() 
{
    // auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    int width = 5;
    int height = 3;
    Robot* obj = new Robot(width, height);

    int num = 2;
    obj->step(num);

    obj->step(num);

    vector<int> param_2 = obj->getPos();
    print_vector(param_2);


    string param_3 = obj->getDir();

    return 0;
}

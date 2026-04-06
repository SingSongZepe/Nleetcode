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

#include <unordered_map>
#include <algorithm>
class Solution {
public:
    template <typename T>
    struct Vec2 {
        T x;
        T y;
        Vec2 operator*(const T& factor) const {
            return Vec2 {
                x * factor,
                y * factor
            };
        }
        Vec2 operator+(const Vec2<T>& v) const {
            return Vec2 {
                x + v.x,
                y + v.y
            };
        }
        void mul(const T& factor) { // int size_t usize32_t ..
            x *= factor;
            y *= factor;
        }
        void add(const Vec2<T>& v) {
            x += v.x;
            y += v.y;
        }
        T max_squared_euclidean_dis() const {
            return x * x + y * y;
        }
    };
    typedef Vec2<int> Position;
    typedef Vec2<int> Dir;

    // north east south west

    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        static constexpr Dir dirs[4] = {Dir{0, 1}, Dir{1, 0}, Dir{0, -1}, Dir{-1, 0}};

        // (x, y1) (x, y2) -> x -> (y1, y2)
        std::unordered_map<int, vector<int>> horizontal;
        std::unordered_map<int, vector<int>> vertical;
        for (const auto& obstacle : obstacles) {
            int x = obstacle[0], y = obstacle[1];
            horizontal[y].emplace_back(x);
            vertical[x].emplace_back(y);
        }
        // sort them for bisect
        for (auto& [x, ys] : horizontal) {
            std::sort(ys.begin(), ys.end());
        }
        for (auto& [y, xs] : vertical) {
            std::sort(xs.begin(), xs.end());
        }
        
        // original position
        Position pos{0, 0};
        // face north
        int dir_idx = 0;
        int mx = 0;

        for (const int command : commands) {
            if (command == -1) {                // turn right
                dir_idx = (dir_idx + 1) % 4;    
            } else if (command == -2) {         // turn left
                dir_idx = (dir_idx + 3) % 4; 
            } else {                            // move
                int x = pos.x, y = pos.y;

                if (dir_idx == 0) { //
                    int actual_step = command;
                    if (vertical.count(x)) {
                        const vector<int>& obs = vertical[x];
                        auto it = std::upper_bound(obs.begin(), obs.end(), y);
                        if (it != obs.end()) {
                            actual_step = std::min(command, *it - y - 1);
                        }
                    }
                    pos.add(dirs[dir_idx] * actual_step);
                } 
                else if (dir_idx == 2) {
                    int actual_step = command;
                    if (vertical.count(x)) {
                        const vector<int>& obs = vertical[x];
                        auto it = std::lower_bound(obs.begin(), obs.end(), y);
                        if (it != obs.begin()) {
                            int obs_y = *std::prev(it);
                            actual_step = std::min(command, y - obs_y - 1);
                        }
                    }
                    pos.add(dirs[dir_idx] * actual_step);
                } 
                else if (dir_idx == 1) { 
                    int actual_step = command;
                    if (horizontal.count(y)) {
                        const vector<int>& obs = horizontal[y];
                        auto it = std::upper_bound(obs.begin(), obs.end(), x);
                        if (it != obs.end()) {
                            actual_step = std::min(command, *it - x - 1);
                        }
                    }
                    pos.add(dirs[dir_idx] * actual_step);
                } 
                else if (dir_idx == 3) {
                    int actual_step = command;
                    if (horizontal.count(y)) {
                        const vector<int>& obs = horizontal[y];
                        auto it = std::lower_bound(obs.begin(), obs.end(), x);
                        if (it != obs.begin()) {
                            int obs_x = *std::prev(it);
                            actual_step = std::min(command, x - obs_x - 1);
                        }
                    }
                    pos.add(dirs[dir_idx] * actual_step);
                }
                mx = std::max(mx, pos.max_squared_euclidean_dis()); 
            }
        }

        return mx;   
    }
};

// better implement
#pragma GCC optimize("Ofast,unroll-loops,inline")
#pragma GCC target("avx2,bmi,bmi2")

static const int _ = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    return 0;
}();

// Используем огромный разреженный массив как хэш-таблицу.
// 65536 — это степень двойки, маска будет летать.
long long ht[65536]; 
const long long EMPTY = -1e15;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        // Быстрое зануление через memset — это SIMD уровень.
        for(int i = 0; i < 65536; ++i) ht[i] = EMPTY;

        for (const auto& obs : obstacles) {
            long long key = ((long long)obs[0] << 32) | (obs[1] & 0xFFFFFFFFLL);
            int h = (unsigned int)(key ^ (key >> 32)) & 65535; // Маска вместо %
            while (ht[h] != EMPTY) h = (h + 1) & 65535;
            ht[h] = key;
        }

        // Направления в константах, чтобы не лезть в память лишний раз
        int x = 0, y = 0, dir = 0;
        int maxDistSq = 0;

        for (int cmd : commands) {
            if (cmd < 0) {
                // Магия: (dir + 1) & 3 — это поворот вправо, (dir + 3) & 3 — влево.
                if (cmd == -1) dir = (dir + 1) & 3;
                else dir = (dir + 3) & 3;
            } else {
                // Кэшируем смещения прямо здесь
                int dx = (dir == 1) ? 1 : (dir == 3 ? -1 : 0);
                int dy = (dir == 0) ? 1 : (dir == 2 ? -1 : 0);
                
                while (cmd--) {
                    int nx = x + dx;
                    int ny = y + dy;
                    long long key = ((long long)nx << 32) | (ny & 0xFFFFFFFFLL);
                    
                    // Ультра-быстрый поиск
                    int h = (unsigned int)(key ^ (key >> 32)) & 65535;
                    bool hit = false;
                    while (ht[h] != EMPTY) {
                        if (ht[h] == key) { hit = true; break; }
                        h = (h + 1) & 65535;
                    }
                    
                    if (hit) break;
                    x = nx; y = ny;
                }
                int cur = x * x + y * y;
                if (cur > maxDistSq) maxDistSq = cur;
            }
        }
        return maxDistSq;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> commands;
    vector<vector<int>> obstacles;

    commands = {4,-1,3};
    obstacles = {};
    result = sol->robotSim(commands, obstacles);
    std::cout << result << std::endl; 

    commands = {4,-1,4,-2,4};
    obstacles = {{2, 4}};
    result = sol->robotSim(commands, obstacles);
    std::cout << result << std::endl;


    return 0;
}

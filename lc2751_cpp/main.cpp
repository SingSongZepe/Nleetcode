#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>
#include <stack>

using std::vector;
using std::string;

template <typename T>
void print_vector_ln(const vector<T>& v) {
    for (const T& item : v) {
        std::cout << item << " ";
    } std::cout << "\n";
}

template <typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    return os << "{" << p.first << ", " << p.second << "}";
}

#include <algorithm>
class Solution {
public:
    // move and clear origin vector
    template <typename T>
    vector<std::pair<uint32_t, T>> make_enumerated_vector(vector<T>& v) {
        vector<std::pair<uint32_t, T>> ev;
        ev.reserve(v.size());

        for (uint32_t i = 0; i < v.size(); i++) {
            ev.emplace_back(i, std::move(v[i]));
        } 
        v.clear();

        return ev;
    }

    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        auto idx_pos = make_enumerated_vector(positions);
        std::sort(idx_pos.begin(), idx_pos.end(), [](const std::pair<uint32_t, int>& a, const std::pair<uint32_t, int>& b) {
            return a.second < b.second;
        });

        std::stack<std::pair<uint32_t, int>> healths_moving_r;

        vector<int> alive_robot(healths.size());
        for (const auto [idx, _] : idx_pos) {
            if (directions[idx] == 'L') { // moving l
                int health_l = healths[idx];
                // collision happened
                while(!healths_moving_r.empty() && health_l > 0) {
                    auto [ridx, health_r] = healths_moving_r.top(); healths_moving_r.pop();
                    if (health_l > health_r) {
                        health_l--;
                    } else if (health_l == health_r) {
                        health_l = -1;
                    } else {
                        health_l = -1;
                        health_r--;
                        healths_moving_r.push({ridx, health_r});
                    }
                }
                if (health_l > 0) { // still alive
                    alive_robot[idx] = health_l;
                } else {
                    alive_robot[idx] = 0;
                }
            } else { // moving r
                healths_moving_r.push({idx, healths[idx]});
            }
        }

        while (!healths_moving_r.empty()) {
            auto [idx, health] = healths_moving_r.top();
            healths_moving_r.pop();
            alive_robot[idx] = health;
        }

        vector<int> result;
        for (int i = 0; i < alive_robot.size(); i++) {
            if (alive_robot[i] > 0) result.emplace_back(std::move(alive_robot[i]));
        }
        
        return result;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    vector<int> result;
    vector<int> positions;
    vector<int> healths;
    string directions;

    positions =  {5,4,3,2,1};
    healths = {2,17,9,15,10};
    directions = "RRRRR";
    result = sol->survivedRobotsHealths(positions, healths, directions);
    print_vector_ln(result);

    positions = {4, 47};
    healths = {15, 24};
    directions = "RR";
    result = sol->survivedRobotsHealths(positions, healths, directions);
    print_vector_ln(result);



    return 0;
}

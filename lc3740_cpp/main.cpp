#include <iostream>
#include <memory>
#include <string.h>
#include <string>
#include <vector>

using std::vector;
using std::string;
using std::max;
using std::min;

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

#include <limits>
using std::abs;
class Solution {
public:
    const int MAX = std::numeric_limits<int>::max();
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        int min_dist = MAX; 
        for (int i = 0; i < n-2; i++) 
        for (int j = i+1; j < n-1; j++) 
        for (int k = j+1; k < n; k++) 
        if (nums[i] == nums[j] && nums[j] == nums[k]) 
        min_dist = std::min(min_dist, abs(i-j)+abs(j-k)+abs(k-i));
               
        return min_dist == MAX ? -1 : min_dist;
    }
};

#include <limits>
class Solution1 {
public:
    const int MAX = std::numeric_limits<int>::max();
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        int min_dist = MAX; 
        for (int i = 0; i < n-2; i++) {
            for (int j = i+1; j < n-1; j++) {
                int moved = false;
                for (int k = j+1; k < n && !moved; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        moved = true;
                        min_dist = std::min(min_dist, 2*k-2*i);
                    }
                }
            }
        }
        return min_dist == MAX ? -1 : min_dist;
    }
};

template <typename T>
__attribute__((pure)) bool larger_(const T& a, const T& b) {
    return a > b;
}
template <typename T>
__attribute__((pure)) bool less_(const T& a, const T& b) {
    return a < b;
}

// the bad design mode
template <typename T>
void sort(vector<T>& x, bool (*op)(const T&, const T&) = larger_<T>) {
    // bubble CBA sorting
    for (int i = 0; i < x.size(); i++) {
        for (int j = 0; j < x.size()-i-1; j++) {
            if (op(x[j+1], x[j])) {
                std::swap(x[j], x[j+1]);
            }
        }
    }
}

template <typename T, typename Compare>
void sort(vector<T>& x, Compare op) {
    for (int i = 0; i < x.size(); i++) {
        for (int j = 0; j < x.size()-i-1; j++) {
            if (op(x[j+1], x[j])) {
                std::swap(x[j], x[j+1]);
            }
        }
    }
}

template <typename T>
struct CompareLarger {
    bool operator()(const T& a, const T& b) const {
        return a > b;
    }
};

#include <chrono>
using namespace std;
using namespace std::chrono;

void run_bench() {
    const int N = 10000;
    vector<int> base(N);
    for(int& i : base) i = rand() % 10000;

    auto v1 = base;
    auto v2 = base;
    auto v3 = base;

    auto s1 = high_resolution_clock::now();
    sort(v1, larger_<int>);
    auto e1 = high_resolution_clock::now();
    cout << "Function Pointer: " << duration_cast<milliseconds>(e1 - s1).count() << "ms\n";

    struct { bool operator()(int a, int b) { return a > b; } } custom_op;
    auto s2 = high_resolution_clock::now();
    sort(v2, custom_op);
    auto e2 = high_resolution_clock::now();
    cout << "Functor Object:   " << duration_cast<milliseconds>(e2 - s2).count() << "ms\n";

    auto s3 = high_resolution_clock::now();
    sort(v3, [](int a, int b) { return a > b; });
    auto e3 = high_resolution_clock::now();
    cout << "Lambda (Inlined): " << duration_cast<milliseconds>(e3 - s3).count() << "ms\n";
}

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    int result;

    vector<int> x{3, 1, 5, 2, 3, 9, 2};
    sort(x);
    print_vector_ln(x);
    sort(x, less_<int>);
    print_vector_ln(x);

    CompareLarger<int> op{};
    sort(x, op);
    print_vector_ln(x);

    run_bench();
    

    return 0;
}

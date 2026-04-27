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
};

// leetcode list node
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void print_list(const ListNode* root) {
    while (root != nullptr) {
        std::cout << root->val << ((root->next != nullptr) ? "->" : "");
        root = root->next;
    }
}

void print_list_ln(const ListNode* root) {
    while (root != nullptr) {
        std::cout << root->val << ((root->next != nullptr) ? "->" : "");
        root = root->next;
    } std::cout << "\n";
}


class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {

        return head;
    }
};

int main() 
{
    auto sol = std::make_unique<Solution>();
    
    int n;
    ListNode* result;
    
    ListNode root = ListNode(1);
    ListNode n2 = ListNode(2);
    ListNode n3 = ListNode(3);
    ListNode n4 = ListNode(4);
    ListNode n5 = ListNode(5);
    root.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;
    int k;
    k = 2;
    print_list_ln(&root);
    result = sol->reverseKGroup(&root, 2);
    print_list_ln(result);
    
    return 0;
}

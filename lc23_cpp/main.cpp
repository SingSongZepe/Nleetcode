#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <queue>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
using std::vector;

typedef ListNode* pNode;

struct CompareListNode {
    bool operator()(const ListNode* n1, const ListNode* n2) {
        return n1->val > n2->val; 
    }
};


class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, vector<ListNode*>, CompareListNode> q;
        
        for (const auto& list : lists) {
            if (list) q.emplace(list);
        }

        ListNode dummy = ListNode();
        ListNode* curr = &dummy;
        while (!q.empty()) {
            ListNode* node = q.top(); q.pop();
            curr->next = node;
            curr = curr->next;
            if (node->next) q.emplace(node->next);
        }
        
        return dummy.next;
    }
};


int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;


    return 0;
}

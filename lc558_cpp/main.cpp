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

// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};


class Solution {
public:
    typedef Node* pNode;

    pNode intersect(pNode qt1, pNode qt2) {
        if (qt1->isLeaf) {
            if (qt1->val) { // true
                return qt1;
            } 
            return qt2;
        }
        if (qt2->isLeaf) {
            if (qt2->val) {
                return qt2;
            }
            return qt1;
        }

        qt1->topLeft = intersect(qt1->topLeft, qt2->topLeft);
        qt1->topRight = intersect(qt1->topRight, qt2->topRight);
        qt1->bottomLeft = intersect(qt1->bottomLeft, qt2->bottomLeft);
        qt1->bottomRight = intersect(qt1->bottomRight, qt2->bottomRight);

        auto tl = qt1->topLeft, tr = qt1->topRight, bl = qt1->bottomLeft, br = qt1->bottomRight;

        if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf ) { // if val == false, shrink to one node
            bool val = tl->val || tr->val || bl->val || br->val;
            bool all_true = tl->val && tr->val && bl->val && br->val;
            qt1->val = val;
            if (!val || all_true) {
                qt1->topLeft = nullptr;
                qt1->topRight = nullptr;
                qt1->bottomLeft = nullptr;
                qt1->bottomRight = nullptr;
                qt1->isLeaf = true;
            }
        }

        return qt1;
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;

    return 0;
}

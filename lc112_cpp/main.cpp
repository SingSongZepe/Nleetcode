#include <iostream>
#include <memory>
#include <string.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false;
        if (!root->left && !root->right) { // leaf node
            if (!(targetSum - root->val)) { // if targetSum is 0
                return true;
            }
        }
        int remainSum = targetSum - root->val;
        return hasPathSum(root->left, remainSum) ||
               hasPathSum(root->right, remainSum);
    }
};

int main() 
{
    auto sol = std::make_shared<Solution>();
    
    int n;
    int result;



    return 0;
}

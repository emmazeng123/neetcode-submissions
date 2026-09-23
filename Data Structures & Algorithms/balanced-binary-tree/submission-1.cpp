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

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr){
        return true;
        }
        // find the height of left sub-tree 
        int left = dfs(root->left);
        // find the height of right sub-tree
        int right = dfs(root->right);
        
        if (abs(left-right)<=1){
            return true;
        }
        else{
            return false;
        }
    }

    private:
    int dfs(TreeNode* node){
        if (node == nullptr){
            return 0;
        }
        
        int left = dfs(node->left);
        int right = dfs(node->right);

        return 1 + max(left,right);
    }
};

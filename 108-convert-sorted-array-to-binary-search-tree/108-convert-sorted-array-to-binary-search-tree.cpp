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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return addNode(nums, 0, nums.size() - 1);
    }
    
private: 
    TreeNode* addNode(vector<int>& nums, int left, int right) {
        if (left > right)
            return NULL;
        int middleIndex = left + ((right - left) / 2);
        TreeNode* tree = new TreeNode(nums[middleIndex]);
        tree->left = addNode(nums, left, middleIndex - 1);
        tree->right = addNode(nums, middleIndex + 1, right);
        return tree;
    }
};
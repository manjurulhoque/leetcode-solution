# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.add(root, low, high, 0)
        
        return self.ans
    
    def add(self, node, low, high, ans):
        if node.left:
            self.add(node.left, low, high, ans)
        
        # print(node.val)
        if node.val >= low and node.val <= high:
            self.ans += node.val
        
        if node.right:
            self.add(node.right, low, high, ans)
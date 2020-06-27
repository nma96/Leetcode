# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # In-place
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
    
    # New tree
        # if not t1:
        #     return t2
        # elif not t2:
        #     return t1
        # else:
        #     res = TreeNode(t1.val + t2.val)
        #     res.left = self.mergeTrees(t1.left, t2.left)
        #     res.right = self.mergeTrees(t1.right, t2.right)
        # return res
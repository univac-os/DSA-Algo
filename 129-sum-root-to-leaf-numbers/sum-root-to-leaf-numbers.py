# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        dfs and add it
        """
        def dfs(root,res):
            if not root:
                return 0
            res=res*10+root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left,res)+dfs(root.right,res)
        return dfs(root,0)
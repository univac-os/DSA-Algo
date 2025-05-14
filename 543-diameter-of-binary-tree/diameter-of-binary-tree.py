# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        find the depth on max both side and add them below failed as the we are considering the largest diameter always passing through root but not in every task
        """
        self.dia=0
        def depth(root):
            if not root:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            self.dia=max(self.dia ,left+right) #check on one side of tree
            return 1 + max(left,right)
        depth(root)
        return self.dia
       
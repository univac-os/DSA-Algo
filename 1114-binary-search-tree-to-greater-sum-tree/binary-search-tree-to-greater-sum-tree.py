# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #post order tranversal LRN but here we need R N L (reverse in order L N R)
        #in N we will add sum +node.val
        currSum=0

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            nonlocal currSum
            node_init_val=node.val
            node.val+=currSum #added to node
            currSum+=node_init_val #add to currSum
            dfs(node.left)

        dfs(root)
        return root
        
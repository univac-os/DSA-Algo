# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        post order transerval LRN 
        calculate max and min from subtree and move up and calculate O(N)
        """
        self.res=0
        def dfs(node):
            if not node:
                return [float('inf'),float('-inf')] #[min,max]
            
            left_mini,left_maxi=dfs(node.left)
            right_mini,right_maxi=dfs(node.right)

            curr_min=min(node.val,left_mini,right_mini)
            curr_max=max(node.val,left_maxi,right_maxi)

            self.res=max(self.res,abs(node.val-curr_min),abs(node.val-curr_max))

            return [curr_min,curr_max]

        dfs(root)
        return self.res
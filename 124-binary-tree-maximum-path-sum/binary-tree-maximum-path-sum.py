# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #dfs to get sub problem so DP
        #each node we want if we split which side needed to take
        #without split take both side 
        #so res variable will have max value
        #return of dfs method will be with split
        res=root.val
        def dfs(node):
            if not node:
                return 0
            leftMax=dfs(node.left)
            rightMax=dfs(node.right)
            #we can have -ve sum as well so not consider them
            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)
            #without split
            nonlocal res
            res=max(res,node.val+leftMax+rightMax)

            #with split
            return node.val+max(leftMax,rightMax)

        dfs(root)
        return res
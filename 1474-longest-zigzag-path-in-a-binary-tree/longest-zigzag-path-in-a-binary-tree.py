# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        #dp dfs  true-left false -right ki po
        def dfs(node,dir,count):
            if node==None:
                return count-1
            if dir:
                left=dfs(node.left,False,count+1)
                right=dfs(node.right,True,1)# start from here
            else:
                right=dfs(node.right,True,count+1)
                left=dfs(node.left,False,1)#start from here
            return max(left,right)
        
        return max(dfs(root,True,0),dfs(root,False,0))
            
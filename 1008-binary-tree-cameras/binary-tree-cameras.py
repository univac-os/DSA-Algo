# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        looks greedy,checking the options
        when both side children have camera and mark the children has viewed,
        if there is one child ,then in that child we need to have camera for sure and make its children can be viewed
        so we need to check children first so LRN (post-order transversal need to know)
        2 options 
        no children covered -- the parent have camera
        a children covered --so parent covered
        2 children no covered --parent need to have
        0-no covered
        1-covered
        2-camera install
        """
        self.camera=0
        def dfs(node):
            if not node:
                return 1 #covered
            left=dfs(node.left)#LR N
            right=dfs(node.right)

            #check anyone has no camera
            if left ==0 or right==0:
                self.camera+=1 
                return 2 #installed
            
            #check both side has camera
            if left==2 or right==2:#so parent covered
                return 1

            #else no one has camera
            return 0
        
        if dfs(root)==0:#both children no camera
            self.camera+=1
        
        return self.camera
        
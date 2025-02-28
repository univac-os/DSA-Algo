# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        1st num in preorder is root,find this num in inord,now left side to this num are the node present on left side 
        How many are there check from 0 to index of root in inorder and use this length to find in postorder form start AND remaining are on right side
        """
        if not preorder or not inorder:
            return None
        #find root
        root=TreeNode(preorder[0])
        root_idx=inorder.index(preorder[0])
        #build left and right
        root.left=self.buildTree(preorder[1:root_idx+1],inorder[:root_idx])
        root.right=self.buildTree(preorder[root_idx+1:],inorder[root_idx+1:])
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxLeft(self,root):
        while root.right:
            root=root.right
        return root
    def helper(self,root):
        #go left subtrees from there find max value[go right] and attach the inital right subtree to it
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        #both side we have node so recursion
        rightChild=root.right
        #find max val on left subtree
        maxLeft=self.findMaxLeft(root.left)
        maxLeft.right=rightChild

        return root.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            return self.helper(root)
        
        return root

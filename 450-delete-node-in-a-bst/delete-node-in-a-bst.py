# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    another solution is find the node and go to right subtree from there find min value (that extreme left) node and replace it and remove this node 
    here we will have one function
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:return root
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            #we found key 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr=root.right
                while curr.left:
                    curr=curr.left
                root.val=curr.val
                #now remove this node
                root.right=self.deleteNode(root.right,curr.val)
        return root
    ###################

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
            return self.helper(root)
        
        return root

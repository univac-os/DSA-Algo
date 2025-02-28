# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        1st num in preorder(NLR) is root,find this num in inord,now left side to this num are the node present on left side 
        How many are there check from 0 to index of root in inorder and use this length to find in postorder form start AND remaining are on right side
        """
        inorder_Idx={v:i for i,v in enumerate(inorder)}
        def helper(l,r):
            if l>r:
                return None
            #find root in inorder
            root=TreeNode(preorder.pop(0))#pop at idx=0
            root_idx=inorder_Idx[root.val]
            #build left and right
            root.left=helper(l,root_idx-1)
            root.right=helper(root_idx+1,r)
            return root
        

        return helper(0,len(inorder)-1)
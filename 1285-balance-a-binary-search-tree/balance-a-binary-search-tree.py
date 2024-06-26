# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #get the sorted array hOW inorder tranversal L N R
        #now on this BST by getting middle element in array everytime  so gives 
        #so diff ht will be 1 as we will distrubute evenly
        def createInorder(node):
            if not node:
                return 
            createInorder(node.left)
            inorder.append(node.val)
            createInorder(node.right)

        inorder=[]
        createInorder(root)
        def createBalanceBST(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            #distrubute evenly
            left_subT=createBalanceBST(l,mid-1)
            right_subT=createBalanceBST(mid+1,r)

            node=TreeNode(inorder[mid],left_subT,right_subT)
            return node

        return createBalanceBST(0,len(inorder)-1)
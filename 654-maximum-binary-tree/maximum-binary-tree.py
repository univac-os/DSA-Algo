# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        1. get index of max val i 
        0..i-->left side. i+1...n -->right side
        again recussion like divide and conquer (qucik sort)
        we need to get max val everytime so recursion
        """
        def get_max(l,r):
            idx=l
            for i in range(l,r):
                if nums[idx]<nums[i]:
                    idx=i
            return idx
        def rec(l,r):
            if l==r:
                return None
            idx=get_max(l,r)
            #0..idx-left side and idx+1..n right side
            node=TreeNode(nums[idx])
            node.left=rec(l,idx)
            node.right=rec(idx+1,r)
            return node
            
        return rec(0,len(nums))
        
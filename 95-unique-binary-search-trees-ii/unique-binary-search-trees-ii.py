# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #check left side right side so recursive
        #looks like dp as sub problem after taking value
        def generate(left,right):
            if left==right:
                return [TreeNode(left)]
            if left>right:
                return [None]
            
            res=[]
            for val in range(left,right+1):
                #take each value in left and right and make combination
                for leftTree in generate(left,val-1):
                    for rightTree in generate(val+1,right):
                        root=TreeNode(val,leftTree,rightTree)
                        res.append(root)
            return  res


        
        return generate(1,n)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        #looking at this example we can see get all child (middle value from []) and check with 1st val
        #idea--> root is 1st value but this value can be child to another look it as graph
        #construct of tree --simple you the condition given

        node={}#create adj list type
        children=set()
        for p,c,l in descriptions:
            children.add(c)
            if p not in node:
                node[p]=TreeNode(p)
            if c not in node:
                node[c]=TreeNode(c)
            
            if l:
                #right node
                node[p].left=node[c]
            else:
                node[p].right=node[c]

        
        for p,c,l in descriptions:
            if p not in children:
                return node[p]
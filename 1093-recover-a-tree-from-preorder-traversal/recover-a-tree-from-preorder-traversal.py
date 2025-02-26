# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        preorder nlr
        based on dashes will be know the depth of that node in tree
        given if single child it will be on left side So meaning we will complete one side and move to 
        other side so using stack length for depth index
        """
        stack=[]
        dashes=0
        i=0
        while i<len(traversal):
            if traversal[i]=="-":
                dashes+=1
                i+=1
            else:
                #we have some value
                j=i
                while j<len(traversal) and traversal[j]!="-":
                    j+=1 #get complete number 
                val=traversal[i:j]
                node=TreeNode(int(val))
                #now we need to append this node to parents but which parent
                while len(stack)>dashes:
                    #we need go up and append it
                    stack.pop()
                #add to left or right
                if stack and not stack[-1].left:
                    stack[-1].left=node
                elif stack:
                    stack[-1].right=node
                
                stack.append(node)
                i=j
                dashes=0 #reset it
        return stack[0]

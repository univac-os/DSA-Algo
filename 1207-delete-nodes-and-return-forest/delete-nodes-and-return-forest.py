# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        #delete the node -->find it if fond then then null else send node
        #but we need to remove the children under it--> how
        #we use hashset and inital add root if we need delete node take the child and add to that hashset
        #why hashset??-->O(1) to add or remove
        to_delete=set(to_delete) #O(1) to find the node in it
        ans=set([root])

        def dfs(node):
            if not node:
                return None
            res=node #no delete node found 
            if node.val in to_delete:
                #we found the delete node return null 
                res=None  #return type
                ans.discard(node) #remove it (does not throw no keyError)
                #add child 
                if node.left: ans.add(node.left)
                if node.right: ans.add(node.right)
            
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            return res


        dfs(root)
        return list(ans)# we want result in list format
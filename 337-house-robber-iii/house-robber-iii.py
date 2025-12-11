# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        two directly-linked houses were broken into on the same night. so ancestor shoudl not be same
        side examples are wrong way for understanding so every step take or not take
        """
        cache={}
        def dfs(node):
            if not node: return 0
            if node in cache:return cache[node]
            #not take
            m_nt=dfs(node.left)+dfs(node.right)
            #take so skip children
            l1,r1=node.val,node.val
            if node.left:
                l1+=dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                r1+=dfs(node.right.left)+dfs(node.right.right)
            m_t=l1+r1-node.val
            
            cache[node]=max(m_nt,m_t)
            return max(m_nt,m_t)

        return dfs(root)
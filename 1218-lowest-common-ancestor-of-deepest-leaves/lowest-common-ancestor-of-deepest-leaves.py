# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        BFS find the children and take first and last children and Use LCA O(n)
        can we do using DFS only in LCA code we can find height as well as we are going down to find the children node
        but if i am doing from top how will know which is children node?--we can use height as parameter to check whether we can find children in going the path
        """
        if not root:return None
        def dfs(node):
            if not node:
                return node,0
            left_node,left_ht=dfs(node.left)
            right_node,right_ht=dfs(node.right)
            if left_ht==right_ht:
                #so children on both side
                return node,1+left_ht #add that node level as well
            elif left_ht>right_ht:
                #left side children are present
                return left_node,1+left_ht
            else:
                #right side more
                return right_node,1+right_ht
            
        node,_=dfs(root)
        return node

        q=deque([root])
        while q:
            level=list(q)
            for _ in range(len(level)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        def LCA(root,p,q):
            if not root or root==p or root==q:
                return root
            left=LCA(root.left,p,q)
            right=LCA(root.right,p,q)
            if left and right:
                return root
            return left if left else right

        return LCA(root,level[0],level[-1])
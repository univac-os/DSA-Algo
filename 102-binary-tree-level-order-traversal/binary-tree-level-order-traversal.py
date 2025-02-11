# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS is better O(n)
        with DFS go till end and backtrack
        """
        if not root:return []
        res=[]
        def dfs(root,level):
            if not root:
                return
            if len(res)==level:#first time
                res.append([])
            res[level].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        return res

        q=deque([root])
        res=[]
        while q:
            lev=[]
            for _ in range(len(q)):
                node=q.popleft()
                lev.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lev)
        return res
               


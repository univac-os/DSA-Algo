# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            level = list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print(level)
        def lca(root, p, q):
            if not root or root == p or root == q:
                return root
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        # Just use first and last nodes
        return lca(root, level[0], level[-1])

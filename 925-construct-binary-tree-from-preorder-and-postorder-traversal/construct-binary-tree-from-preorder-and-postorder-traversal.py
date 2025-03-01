# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        1st num in pre and last num is root
        next 2nd num in pre is left start and -2 num is right start
        find the 2nd num index in post so we get that many num are present in left side
        """
        n = len(preorder)
        post_idx = {val: i for i, val in enumerate(postorder)}
        
        def helper(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None
            root = TreeNode(preorder[i1])#starting node is root
            if i1 == i2:
                return root
            # Find left subtree root node (second element in preorder)
            left_root_val = preorder[i1 + 1]
            left_idx = post_idx[left_root_val]
            left_size = left_idx - j1 + 1  # Number of nodes in left subtree

            # Construct left and right subtrees
            root.left = helper(i1 + 1, i1 + left_size, j1, left_idx)
            root.right = helper(i1 + left_size + 1, i2, left_idx + 1, j2 - 1)

            return root

        return helper(0, n - 1, 0, n - 1)

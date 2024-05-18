# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        #DFS post order to get children coins/requirement
        #how many to send left ,right --find height of subtree
        # if 0 return -1 as it wants coin 
        #if 4 return 4-1 as it consume 1 coin
        #in res add extra coins if its -ve add it as it takes from above
        self.res=0
        def dfs(curr):
            if not curr:
                return 0 
            l_ht=dfs(curr.left)
            r_ht=dfs(curr.right)
            extra_coins=(curr.val-1) + l_ht +r_ht
            self.res+=abs(extra_coins)
            return extra_coins
            
        dfs(root)
        return self.res

        
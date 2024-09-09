# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,ll,tn):#linkedlist ,treenode
        if not ll:
            return True
        if not tn or ll.val!=tn.val:
            return False
        return (self.dfs(ll.next,tn.left) or self.dfs(ll.next,tn.right))

    def isSubPath(self, LL: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        #dfs check but here linked list start can from tree head or tree head left or right side
        #we want recursion call on both side as well if wont find from head itself
        #check present from head or not
        if self.dfs(LL,root):
            return True
        if not root:
            return False #moved in one direction and cannot find 
        return (self.isSubPath(LL,root.left) or self.isSubPath(LL,root.right))
        
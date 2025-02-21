# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self,root):
        self.nodes=set()
        self.bfs(root)
    def find(self,target):
        return target in self.nodes
    def bfs(root,val):
        q=deque([root])
        root.val=0
        while q:
            node=q.popleft()
            self.nodes.add(root.val)
            if node.left:
                node.left.val=node.val*2+1
                q.append(node.left)
            if node.right:
                node.right.val=node.val*2+2
                q.append(node.right)
        
    #DFS
    def __init__(self, root: Optional[TreeNode]):
        #construct of tree
        self.nodes=set()#add complete node values in set
        self.dfs(root,0)

    def find(self, target: int) -> bool:
        return target in self.nodes #O(1)
    
    def dfs(self,root,val):
        if root is None:
            return
        self.nodes.add(val)
        self.dfs(root.left,val*2+1)
        self.dfs(root.right,val*2+2)



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
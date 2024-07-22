# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        #make tree to graph and from leaf node do bfs and get pairs
        self.pair=0
        adj=defaultdict(list)
        leaves=set()

        def buildGraph(node):#build and get leaf node
            if not node:
                return 
            if not node.left and not node.right:
                leaves.add(node)
            if node.left:
                adj[node.left].append(node)
                adj[node].append(node.left)
            if node.right:
                adj[node.right].append(node)
                adj[node].append(node.right)
            buildGraph(node.left)
            buildGraph(node.right)
        
        def bsf(node):
            q=deque([(node,0)])
            visit=set([node])
            while q:
                n,dis=q.popleft()
                if n!=node and n in leaves and dis<=distance:
                    #we got a pair
                    self.pair+=1
                for nei in adj[n]:
                    if nei not in visit and dis+1<=distance:
                        visit.add(nei)
                        q.append((nei,dis+1))
            
        buildGraph(root)
        for leaf in leaves:
            bsf(leaf)
        
        return self.pair//2
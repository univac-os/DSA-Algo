class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        """
        each point backtrack,can we use heap? get max value at node based on min distance 
        simple backtracking works good
        """
        adj=defaultdict(list)
        for u,v,t in edges:
            adj[u].append((v,t))
            adj[v].append((u,t))

        res=0
        def backtrack(node,time,visit,curr):
            nonlocal res
            if time>maxTime:
                return 0
            if node==0:
                res=max(res,curr)
            for nei,t in adj[node]:
                add=0
                if nei not in visit:
                    visit.add(nei)
                    add=values[nei]
                backtrack(nei,time+t,visit,curr+add)
                if add>0:
                    visit.remove(nei)
                
        backtrack(0,0,set([0]),values[0])
        return res
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        paths checking looks dp
        dfs and find max count check from each node (so new visit set)
        directed graph and need to check cycle as well so we want the dependencies on the node
        topo sort will give cycle present or not
        """
        #1.in edges
        n=len(colors)
        adj=defaultdict(list)
        indeg=[0]*n
        for src,dst in edges:
            adj[src].append(dst)
            indeg[dst]+=1
        dp=[[0]*26 for _ in range(n)] # col X node get max 

        #start from all node where indeg =0 (that will be start point)
        q=deque()
        for i in range(n):
            if not indeg[i]:
                q.append(i)
                dp[i][ord(colors[i])-ord('a')]=1 
        
        res,visit=0,set()
        while q:
            node=q.popleft()
            visit.add(node)
            for v in adj[node]:
                for c in range(26):
                    curr=dp[node][c] #get of color node
                    if c==ord(colors[v])-ord('a'):
                        curr+=1
                    dp[v][c]=max(dp[v][c],curr)
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
            res=max(res,max(dp[node]))
        return res if len(visit)==n else -1


        
        
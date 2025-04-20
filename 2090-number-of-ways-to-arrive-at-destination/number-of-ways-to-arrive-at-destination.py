class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        djastra algo to find min cost path BUT here we can have multiple path with min cost
        SO can be DP at each node we want to find min cost and path and add that if you going to next node
        subproblem 2 cases if any point we find less cost that present at that node then update it
        if same then we want to add the path to get there
        if more we ignore it
        """
        mod=10**9+7
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))
        minH=[(0,0)] #(cost,node)
        min_cost=[float('inf')]*n
        path_count=[0]*n
        path_count[0]=1 #init

        while minH:
            cost,node=heappop(minH)
            #check the cases
            for neiC,nei in adj[node]:
                if neiC+cost<min_cost[nei]:
                    #update the new min cost and path count and add to heap
                    min_cost[nei]=neiC+cost
                    path_count[nei]=path_count[node]#ignore all and fix to this path
                    heappush(minH,(neiC+cost,nei))
                elif neiC+cost==min_cost[nei]:
                    #update the path count
                    path_count[nei]=(path_count[node]+path_count[nei])%mod

        return path_count[n-1]

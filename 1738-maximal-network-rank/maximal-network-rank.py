class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        #find in degree and check pair i1+i2-1 (common for both)
        maxRank=0
        adj=defaultdict(list)
        for r in roads:
            adj[r[0]].append(r[1]) #create adj list 
            adj[r[1]].append(r[0])
        
        for n1 in range(n):# 0-1 0-2 0-3 1-2..
            for n2 in range(n1+1,n):
                currR=(len(adj[n1])+len(adj[n2]))
                if n2 in adj[n1]:# there is connection between pair -1 for common route
                    currR-=1
                
                maxRank=max(maxRank,currR)
        
        return maxRank
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        dijastra algo find least way ,can we use topo (no beacuse DAG needed) so dp store at each point best
        """
        adj=defaultdict(list)
        for s,d,dist in flights:
            adj[s].append((d,dist))
        q=[(0,src,0)]#(dist,node,stops)
        visited=[float('inf')]*n# stops at each node
        while q:
            dist,node,stops=heapq.heappop(q)
            if node==dst:
                return dist
            if stops>k or stops>=visited[node]:
                continue #skip the path
            visited[node]=stops
            for nxt,d in adj[node]:
                heapq.heappush(q,(dist+d,nxt,stops+1))
        return -1
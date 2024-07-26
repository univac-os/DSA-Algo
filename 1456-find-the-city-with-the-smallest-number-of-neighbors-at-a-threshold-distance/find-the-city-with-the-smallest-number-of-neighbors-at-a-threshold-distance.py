class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # bfs or dfs we need how many node it can reach so BFS
        #we need minimum path so minHeap Dijastra algo
        adj=defaultdict(list)
        for v1,v2,dist in edges:
            adj[v1].append((v2,dist))
            adj[v2].append((v1,dist))
        
        def dijkstra(src):
            minH=[(0,src)]# (dist,node)
            visit=set()
            while minH:
                dist,node=heapq.heappop(minH)
                if node not in visit:
                    visit.add(node)
                    for nei,nei_dist in adj[node]:
                        curr_dist=dist+nei_dist
                        if curr_dist<=distanceThreshold:
                            heapq.heappush(minH,(curr_dist,nei))
                
            
            return len(visit)-1 #not take src 
        
        res,min_count=-1,float('inf')
        for src in range(n):
            count=dijkstra(src)
            if count<=min_count:
                res,min_count=src,count

        return res
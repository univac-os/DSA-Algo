class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        Alice has choices
        Bob has no choices
        we have n node and n-1 edges so cycle are not possible
        for bob we need to go to root so make it graph
        Bob DFS we need time as well to know you come first so have a hashmap
        Alice BFS and take better path
        how to find the leaf ? if adj[leaf] has 1 node only (that its parent)
        """
        adj=defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        #BOB time calculate
        bob_times={}#node--> time
        def dfs(node,prev,time):
            if node==0:#root node
                bob_times[node]=time
                return True
            for nei in adj[node]:
                if nei ==prev:
                    continue
                if dfs(nei,node,time+1):
                    bob_times[node]=time
                    return True
            return False
        dfs(bob,-1,0)

        #ALICE check BFS
        q=deque([(0,0,-1,amount[0])])#node,time,prev,total_profit
        res=float("-inf")
        while q:
            node,time,prev,profit=q.popleft()
            for nei in adj[node]:
                if nei==prev:
                    continue
                nei_profit=amount[nei]
                nei_time=time+1
                #check how came first
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        #bob came first so make it 0
                        nei_profit=0
                    elif nei_time==bob_times[nei]:
                        #both at a time so half to each
                        nei_profit=nei_profit//2
                q.append((nei,nei_time,node,nei_profit+profit))
                if len(adj[nei])==1:
                    res=max(res,nei_profit+profit)
        return res

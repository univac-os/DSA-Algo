class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #look as graph adj list is need
        #take leaves node or root node ?
        #root node then dfs till all visited and get the height
        #leave node --go up till root and get root --this is BETTER
        if n==1:
            return [0]
        adjl=defaultdict(list)
        for n1,n2 in edges:
            adjl[n1].append(n2)
            adjl[n2].append(n1)
        
        edge_cnt={}#each node how many are connected
        leaves=deque()
        for src,nei in adjl.items():
            if len(nei)==1:
                #this is leaf
                leaves.append(src)
            edge_cnt[src]=len(nei)
        
        #start from leave go to root
        while leaves:
            if n<=2:#if only 2 root then same level
                return list(leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                #now remove the edge to its nei --going up
                for nei in adjl[node]:
                    edge_cnt[nei]-=1
                    if edge_cnt[nei]==1:
                        #we got new above level
                        leaves.append(nei)



        
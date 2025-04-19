class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        we are components so discrete graph and find cycle is solution NO
        COMPLETE GRAPH have edge n*(n-1)/2 [directed] for undirected n*(n-1)
        so for each node n*(n-1)/n edges are there so n-1 edges are present
        so we can use dfs and find the component and find its have required edges or not 
        so we need adj list to know the edges count
        """
        adj=defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(n,nodes):
            if n in visit:
                return
            visit.add(n)
            nodes.append(n)
            for nei in adj[n]:
                dfs(nei,nodes)
            return nodes
        
        res=0
        visit=set()
        for v in range(n):
            if v in visit:
                continue
            comp=dfs(v,[])#we have comp list
            if all(len(comp)-1 ==len(adj[n]) for n in comp ): #n-1==edge going out from that node
                res+=1
        return res
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        n node n edges so pakka cycle is there so we need to find cycle in this 
        then the edge which causes cycle O(V+E)
        use UNION FIND by RANK for cycle detection
        """
        N=len(edges)
        par=[_ for _ in range(N+1)]#init each one is its own parent
        rank=[1]*(N+1)

        def find(n):
            #recusion we want to find the parent of node
            if n!=par[n]:
                par[n]=find(par[n])
            return par[n]

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:return False #same parent so cycle is there
            #update the rank and parent 
            if rank[p1]>=rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]

            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
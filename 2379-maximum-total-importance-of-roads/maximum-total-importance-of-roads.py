class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #check edges to each node
        #which node has more that we the more value --GREEDY
        #the num in nodes are not required 
        #so the given wt is distributed in that many degree its connected so edege*wt
        #see example 5 is shown 4 times in the sum calculation
        edges=[0]*n
        for u,v in roads:
            edges[u]+=1
            edges[v]+=1
        edges.sort() #O(nlogn)

        wt=1
        res=0
        for e in edges:
            res+=e*wt
            wt+=1
        return res
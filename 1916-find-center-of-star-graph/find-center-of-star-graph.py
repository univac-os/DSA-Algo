class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #check incoming edge for each node
        #create adj list and check the edge
        adjl=defaultdict(int)
        for e in edges:
            adjl[e[0]]+=1
            adjl[e[1]]+=1
        for node,count in adjl.items():
            if count==len(edges):
                return node
        return -1

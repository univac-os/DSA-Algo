class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        draw graph 
        find dfs for each one and stoe in hashmap
        now from queries check if it present or not O(E+v) here e can be max N^2 so we run O(N*(E+V))
        O(N^3) + O(q)
        """
        def dfs(cr):
            if cr not in Par_Map:
                #create a new set for this
                Par_Map[cr]=set()
                #start check from inital prerequirte node
                for pr in adjList[cr]:
                    #we want union of all node from set
                    # Par_Map[cr] = Par_Map[cr] | dfs(pr)
                    Par_Map[cr].update(dfs(pr))
                #we need to add init prerequirtes node as well 
                Par_Map[cr].add(cr) #every node itself prerequiste

            return Par_Map[cr]


        adjList=defaultdict(list)
        for pr,cr in prerequisites:
            adjList[cr].append(pr)
        #we got inital prerequites for each node
        #now find more deeper

        Par_Map={} # node --> flow of nodes from inintal prerequiste node
        for cr in range(numCourses):
            dfs(cr) #in this we make hashmap

        res=[]
        for pr,cr in queries:
            res.append(pr in Par_Map[cr])
        return res


        
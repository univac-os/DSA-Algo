class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        graph
        check cycle as well how use visit set
        all nodes need to visited
        the final node should have no out degree
        start from node where indegree is 0 node so graph can be discrete 
        like topo sort we need to include if indeg are 0
        BFS as we are node connected to it at a time
        """
        #find indegree=0 node 
        adj=defaultdict(list)
        indeg={}
        for _ in range(numCourses):
            indeg[_]=0

        for child,par in prerequisites:
            adj[par].append(child)
            indeg[child]+=1
        #now we need transver the path based on indeg
        q=deque()
        for k,v in indeg.items():
            if v==0:
                q.append(k)
        topo=[]
        while q:
            course=q.popleft()
            topo.append(course)
            for nei in adj[course]:
                indeg[nei]-=1 # we have completed one task
                if indeg[nei]==0:
                    #this course can added to q as all prereq are done
                    q.append(nei)
        return len(topo)==numCourses
            
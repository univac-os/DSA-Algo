class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        """
        BFS we want max group so BFS at every node
        cycle in example cycle has length 4(even) --No problem
        odd len -->problem because 2 node will have same group number and we want diff =1
        so if odd len cycle return -1
        O(n+n)*n->O(n2)
        #1.find connected graph
        #2.bfs on each connected node
        """
        def get_connected_comp(src):
            q=deque([src])
            component=set([src])
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)#global hashset 
            return component

        def get_longest(src):
            #BFS
            q=deque([(src,1)])#node,group_number
            dist={src:1}#node--> group_number 
            max_gp=0
            while q:
                node,gp=q.popleft()
                for nei in adj[node]:
                    #find cycle 
                    if nei in dist:
                        if dist[nei]==gp: #same group number so diff=0
                            return -1
                        continue
                
                    q.append((nei,gp+1))#into new group
                    dist[nei]=gp+1
            return max(dist.values())

        adj=defaultdict(list)
        for src,dist in edges:
            adj[src].append(dist)
            adj[dist].append(src)
        visit=set()
        res=0

        for i in range(1,n+1):
            if i in visit:
                continue
            visit.add(i)
            comp=get_connected_comp(i)
            
            max_cnt=0
            for src in comp:
                length=get_longest(src)
                if length==-1:#if cycle has odd len
                    return -1
                max_cnt=max(max_cnt,length)
            
            res+=max_cnt #get all groups which are not connected
            
        return res
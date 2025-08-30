class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        need to create graph with bus number has index to know how many bus need to take
        """
        if source==target:return 0
        bus_map=defaultdict(list)
        for bus_no,buses in enumerate(routes):
            for stop in buses:
                bus_map[stop].append(bus_no) #bus --> bus_index
        
        #create graph where we will have bus index of source ,so he can travell all node in that route of source
        q=deque()
        visit=set() #bus index is added 
        for bus in bus_map[source]:
            q.append((bus,1)) # bus_index ,bus_taken
            visit.add(bus)
       
        while q:
            bus_idx,bus_taken=q.popleft()
            for stop in routes[bus_idx]:
                if stop==target:
                    return bus_taken
                for nxt_bus_idx in bus_map[stop]:
                    if nxt_bus_idx not in visit:
                        q.append((nxt_bus_idx,bus_taken+1))
                        visit.add(nxt_bus_idx)
        return -1
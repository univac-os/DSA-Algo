class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #dfs,visited array is not need as we pop from adj list 
        adj=defaultdict(list)
        tickets.sort()#order is needed
        for src,dest in tickets:
            adj[src].append(dest)
        
        res=["JFK"] # start 
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in adj:#no out degree
                return False
            #moves to next node
            temp=list(adj[src])
            for ind,node in enumerate(temp):
                adj[src].pop(ind)# pop it
                res.append(node)
                if dfs(node):
                    return True
                #if false backtrack
                adj[src].insert(ind,node)
                res.pop()
            
            return False

        dfs("JFK")
        return res
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #given 2 island we need to travel so bfs to reach to another island
        #but how to find an island so dfs on it 
        #then bfs to reach another island
        n=len(grid)
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        def invalid(r,c):
            return r<0 or c<0 or r==n or c==n

        visit=set()
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return
            visit.add((r,c))
            for dx,dy in dir:
                dfs(r+dx,c+dy)
    
        def bfs():
            res=0
            q=deque(visit) #add the 1st island
            while q:
                for i in range(len(q)):
                    r,c =q.popleft()
                    for dx,dy in dir:
                        if invalid(r+dx,c+dy) or (r+dx,c+dy) in visit:
                            continue
                        if grid[r+dx][c+dy]:
                            #found another island
                            return res
                        q.append((r+dx,c+dy))
                        visit.add((r+dx,c+dy))
                res+=1 

        for r in range(n):
            for c in range(n):
                #find the an island
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
                
        
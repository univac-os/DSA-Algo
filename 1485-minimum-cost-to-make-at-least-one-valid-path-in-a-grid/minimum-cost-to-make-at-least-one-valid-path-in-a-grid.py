class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        min cost we can use djastra algo priority queue O(nmlogk)
        but observing we can we see cost inceases by 1 if needed
        so we can use queue if same cost add to left 
        if cost+1 add to right so that we will alway take min cost from left everytime 
        similar to djastra algo but here we are specify the order of insertion O(nm)
        """
        direction={1:[0,1],2:[0,-1],3:[1,0],4:[-1,0]}
        row,col=len(grid),len(grid[0])
        q=deque([(0,0,0)])# (r,c,cost)
        visit={(0,0):0} # (r,c)->cost
        while q:
            r,c,cost=q.popleft()
            if (r,c)==(row-1,col-1):
                return cost

            for d in direction:
                dr,dc=direction[d]
                nr,nc=r+dr,c+dc
                n_cost=cost if d==grid[r][c] else cost+1

                if (nr<0 or nc<0 or nr==row or nc ==col or n_cost>=visit.get((nr,nc),float('inf')) ):
                    #if we came to that box with less cost then that path is not minimum
                    continue
                visit[(nr,nc)]=n_cost
                
                if d==grid[r][c]:
                    q.appendleft((nr,nc,n_cost))
                else:
                    q.append((nr,nc,n_cost))
        
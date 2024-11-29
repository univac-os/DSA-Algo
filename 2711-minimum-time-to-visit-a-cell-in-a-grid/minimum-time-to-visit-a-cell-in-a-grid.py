class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        here bfs instead of queue we use priortyQueue why? we want minimum value
       cases PATTERN
       1. 5 | 5 --> diff 0 so next block +1 =5+1
       2. 4 | 5 --> diff 1 so next block  =5
       3. 3 | 5 --> diff 2 so move back froth (3+2)=5 now diff is 0 so next block +1 =5+1
       4. 2 | 5 --->diff 3 so move backfront (2+2)=4 now diff is 1 so next block =5
        """
        if min(grid[0][1],grid[1][0])>1:
            return -1
        minH=[(0,0,0)] #(time,r,c)
        row,col=len(grid),len(grid[0])
        visit=set()
        while minH:
            t,r,c=heapq.heappop(minH)
            if (r,c)==(row-1,col-1):
                return t
            nei=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in nei:
                if nr<0 or nc<0 or nr==row or nc==col or (nr,nc) in visit:
                    continue
                extra=0
                if abs(grid[nr][nc]-t)%2==0:
                    extra=1
                nxt_time=max(grid[nr][nc]+extra,t+1)
                heapq.heappush(minH,(nxt_time,nr,nc))
                visit.add((nr,nc))
        
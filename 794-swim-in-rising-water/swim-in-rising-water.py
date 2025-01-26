class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        graph , BFS with minHeap so Dijastra algo 
        modified version we take max till that position O(n2logn)
        """
        N=len(grid)
        visit=set()
        minH=[(grid[0][0],0,0)]#(time,r,c)
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        visit.add((0,0))
        while minH:
            t,r,c=heapq.heappop(minH)
            if r==N-1 and c==N-1:
                return t
            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if 0<=nr<N and 0<=nc<N and (nr,nc) not in visit:
                    heapq.heappush(minH,( max(t,grid[nr][nc]) ,nr,nc ))
                    visit.add((nr,nc))
        
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        djastra algo but how can i find till that point this diff is mini so store it
        """
        row,col=len(heights),len(heights[0])
        dir=[(0,-1),(0,1),(1,0),(-1,0)]
        mat=[[float('inf')]*col for _ in range(row)]
        mat[0][0]=0
        min_h=[(0,0,0)] #diff,r,c
        while min_h:
            diff,r,c=heapq.heappop(min_h)

            if r==row-1 and c==col-1:
                return diff
            for dr,dc in dir:
                nr,nc =r+dr,c+dc
                if 0<=nr<row and 0<=nc<col:
                    new_diff=max(diff,abs(heights[r][c]-heights[nr][nc]))
                    if new_diff<mat[nr][nc]:
                        #found mini
                        mat[nr][nc]=new_diff
                        heapq.heappush(min_h,(new_diff,nr,nc))
        
        
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        #greedy --NOOOO as start/end is not a start or last row
        #brute force check eachone and backtrack it O(m*n* 4**(m*n))
        #check the visited also-- simple visit it and make it 0 and again to normal
        row,col=len(grid),len(grid[0])
        res=0

        def backTrack(r,c):
            if  min(r,c)<0 or r==row or c==col or grid[r][c]==0: return 0
            org_val=grid[r][c]
            #visited 
            grid[r][c]=0
            res =0
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for dx,dy in nei:
                res=max(res,org_val+backTrack(dx,dy))
            #backtracking
            grid[r][c]=org_val
            return res


        for r in range(row):
            for c in range(col):
                res=max(res,backTrack(r,c))
        return res
        
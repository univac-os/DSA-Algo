class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        #GREEDY -- give 1 to start of row beacuse that bit is more than total of remaining
        #for colums check count of 1 and 0 and swap them
        #take O(m*n)
        row,col=len(grid),len(grid[0])
        #flip row
        for r in range(row):
            if grid[r][0]==0:
                for c in range(col):
                    #swap
                    grid[r][c]=0 if grid[r][c] else 1
        #flip col check count 
        for c in range(col):
            one_cnt=0
            for r in range(row):
                one_cnt+=grid[r][c]
            if one_cnt<row-one_cnt:
                #more 0 then swap
                for r in range(row):
                    grid[r][c]=0 if grid[r][c] else 1
        #calculate
        res=0
        for r in range(row):
            for c in range(col):
                res+=grid[r][c]<<(col-1-c) #LEFT SHIFT
        return res
        
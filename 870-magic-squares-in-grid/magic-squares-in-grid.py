class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        #O(n^2) space is O(1) simple check sum of row ,col,diag and give out result
        row,col=len(grid),len(grid[0])
        res=0
        def magic(r,c):
            #check valid set is present (1-9)
            values=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not (1<=grid[i][j]<=9): return 0
                    values.add(grid[i][j])
            # check sum of row
            for i in range(r,r+3):
                if sum(grid[i][c:c+3])!=15:
                    return 0
            # check sum of col
            for i in range(c,c+3):
                if (grid[r][i] + grid[r+1][i] + grid[r+2][i])!=15:
                    return 0
            #check sum of diagional
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]!=15) or (grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]!=15):
                return 0
            return 1

        for r in range(row-2):
            for c in range(col-2):
                res+=magic(r,c)
        return res

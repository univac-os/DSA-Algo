class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        #Optimzed dp 
        prev_dp=[[0]*col for _ in range(col)]
        for r in reversed(range(row)):
            curr_dp=[[0]*col for _ in range(col)]
            for c1 in range(col-1):
                for c2 in range(c1+1,col):
                    max_cherries=0
                    cherry=grid[r][c1]+grid[r][c2]
                    for c1_d,c2_d in product([-1,0,1],[-1,0,1]):
                        nc1,nc2=c1+c1_d,c2+c2_d
                        if nc1<0 or nc2 ==col:
                            continue
                        max_cherries=max(max_cherries,cherry+prev_dp[nc1][nc2])
                    
                    curr_dp[c1][c2]=max_cherries
            prev_dp=curr_dp
        
        return prev_dp[0][col-1]
        #memorization
        cache={}
        def dfs(r,c1,c2):
            if (r,c1,c2) in cache:
                return cache[(r,c1,c2)]
            #extreme points
            if c1==c2 or min(c1,c2)<0 or max(c1,c2)==col:
                return 0
            if r==row-1:
                return grid[r][c1]+grid[r][c2]
            #3*3 directions
            res=0
            for c1_d in [-1,0,1]:
                for c2_d in [-1,0,1]:
                    res=max(res,dfs(r+1,c1+c1_d,c2+c2_d))
            cache[(r,c1,c2)]=res+grid[r][c1]+grid[r][c2]
            return cache[(r,c1,c2)]

        return dfs(0,0,col-1)
        
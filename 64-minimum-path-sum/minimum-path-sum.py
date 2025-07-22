class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp each position 2 options 
        """
        n,m=len(grid),len(grid[0])

        dp=[[float('inf')]*(m+1)]*(n+1)
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i==n-1 and j==m-1:dp[i][j]=grid[i][j]
                else:dp[i][j]=min(dp[i][j+1],dp[i+1][j])+grid[i][j]

        return dp[0][0]

        cache={}
        def dfs(i,j):
            if i==n or j==m:return float('inf')
            if i==n-1 and j==m-1: return grid[i][j]
            if (i,j) in cache: return cache[(i,j)]
            right=dfs(i,j+1)
            down=dfs(i+1,j)
            cache[(i,j)]=min(right,down)+grid[i][j]
            return cache[(i,j)]

        return dfs(0,0)

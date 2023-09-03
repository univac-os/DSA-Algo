class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def dfs(i,j):
            if i==0 and j==0:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            if i<0 or j<0:
                return 0
            up=dfs(i-1,j)
            left=dfs(i,j-1)
            dp[(i,j)]=up+left
            return dp[(i,j)]

        
        return dfs(m-1,n-1)
        dp=[[1]*n for _ in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[m-1][n-1]


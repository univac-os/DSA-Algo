class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        #inplace so bottom is taken ,take left side
        dp=[0]*(n)
        dp[n-1]=1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c]=0
                elif c+1<n:#bottom+left
                    dp[c]=dp[c]+dp[c+1]
                else:
                    dp[c]=dp[c]+0#only bottom

        return dp[0]
         
        dp={}
        def countPath(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]==1 :
                return 0
            if(i,j) in dp:
                return dp[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            dp[(i,j)]=countPath(i+1,j) + countPath(i,j+1)
            return dp[(i,j)]
        return countPath(0,0)
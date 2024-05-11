class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # looks dp as subproblem so check down,right,diagonal
        # bottom up DP 
        if not matrix:
            return 0
        
        row,col=len(matrix),len(matrix[0])
        dp=[[0]*(col+1) for _ in range(row+1)]
        max_val=0
        #base case not needed actually as we have taken care above col+1 and row+1 
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if matrix[r][c]=="1":
                    down=dp[r+1][c]
                    right=dp[r][c+1]
                    diag=dp[r+1][c+1]
                    dp[r][c]=1+min(down,right,diag)
                    max_val=max(max_val,dp[r][c])
        return max_val**2
        
        
        # memo O(m*n) space O(m*n) top down
        row,col=len(matrix),len(matrix[0])
        cache={} #(r,c)-->max side of square
        def helper(r,c):
            if r>=row or c>=col:
                return 0
            if (r,c) not in cache:
                down=helper(r+1,c)
                right=helper(r,c+1)
                diag=helper(r+1,c+1)
                cache[(r,c)]=0
                if matrix[r][c]=="1":
                    cache[(r,c)]=1+min(down,right,diag)

            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values())**2
        
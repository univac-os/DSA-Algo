class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        DP from a point check 3 directions down,left,diagonal this is how many we can form from that point O(n2)
        '''
        #BOTTTOM UP 
        row,col=len(matrix),len(matrix[0])
        dp=[[0]*col for _ in range(row)]
        res=0
        for r in reversed(range(row)):
            for c in reversed(range(col)):
                if matrix[r][c] == 1:
                    if r == row - 1 or c == col - 1:
                        dp[r][c] = 1  # Edge cells, no square beyond them
                    else:
                        dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
                    res += dp[r][c]
        return res       


        row,col=len(matrix),len(matrix[0])
        cache={}            
        def dfs(r,c):
            if r==row or c==col or not matrix[r][c]:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            count=1+min(dfs(r+1,c),dfs(r,c+1),dfs(r+1,c+1))
            cache[(r,c)]=count
            return cache[(r,c)]
        res=0
        for r in range(row):
            for c in range(col):
                res+=dfs(r,c)
        return res
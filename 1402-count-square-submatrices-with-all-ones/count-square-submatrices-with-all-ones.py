class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        DP from a point check 3 directions down,left,diagonal this is how many we can form from that point O(n2)
        '''
        #BOTTTOM UP 
        row, col = len(matrix), len(matrix[0])
        prev = [0] * (col + 1)
        res = 0
        
        for r in reversed(range(row)):
            curr = [0] * (col + 1)
            for c in reversed(range(col)):
                if matrix[r][c] == 1:
                    curr[c] = 1 + min(prev[c], prev[c + 1], curr[c + 1])
                    res += curr[c]
            prev = curr  
        
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
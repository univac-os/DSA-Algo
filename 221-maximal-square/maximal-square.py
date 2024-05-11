class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # looks dp as subproblem so check down,right,diagonal
        
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
        
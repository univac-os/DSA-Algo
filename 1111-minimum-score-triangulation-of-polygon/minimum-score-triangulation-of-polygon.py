class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        sort cant do at its polygon with sides,
        without sorting how?
        divide the polygon such that we get 3 points 
        """
        cache={}

        def dfs(i,j):
            if j-i<2:
                return 0 # we cant make triangle
            if j-i==2:
                cache[(i,j)]=values[i]*values[i+1]*values[j]
                return cache[(i,j)]
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)]=min(values[i]*values[k]*values[j]+dfs(i,k)+dfs(k,j) for k in range(i+1,j))
            return cache[(i,j)]
            
        n=len(values)
        return dfs(0,n-1)
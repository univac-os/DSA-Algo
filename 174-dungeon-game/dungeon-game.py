class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        2 option path with less value is good
        greedy wont work here explore all path but we value -ve which is less in magnitude 
        if that val is -ve +1 or else 
        """
        n,m=len(dungeon),len(dungeon[0])
        cache={}
        def dfs(i,j):
            if i>=n or j>=m:return float('inf')
            if (i,j) in cache:return cache[(i,j)]
            if i==n-1 and j==m-1:
                #need + cell>=1
                #if +ve cell then we no need some val so 1 if -ve so we need >= 1-cell
                return max(1,1 - dungeon[i][j]) 

            right=dfs(i,j+1)
            down=dfs(i+1,j)
            min_till_now=min(right,down)
            #above_val +cell >=1
            max_need=max(1,min_till_now-dungeon[i][j])
            cache[(i,j)]=max_need
            return max_need
        return dfs(0,0)
            
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N=len(grid)
        #if we check carefully we only need 2 min values in that row =GREEDy O(n2) space O(1)
        #but how to do get min value and check in between and keep the best 2  min value 
        def get_min_two(row):
            #we send val,idx 
            two_smallest=[]
            for val,idx in row:
                if len(two_smallest)<2:
                    two_smallest.append((val,idx))
                elif two_smallest[1][0]>val:
                    #remove and add the min val
                    two_smallest.pop()
                    two_smallest.append((val,idx))
                two_smallest.sort() #--O(1) as len is 2
            return two_smallest
        first_row=[(val,idx) for idx,val in enumerate(grid[0])]
        dp=get_min_two(first_row)#we can start with this
        for r in range(1,N):
            next_dp=[] #val,idx
            for curr_c in range(N):
                curr_val=grid[r][curr_c]
                min_val=float('inf')
                for prev_val,prev_c in dp:
                    if prev_c!=curr_c:
                        min_val=min(min_val,prev_val+curr_val)
                next_dp.append((min_val,curr_c)) #add the min val in dp and get 2 min
                next_dp=get_min_two(next_dp)
            dp=next_dp
        return min([val for val,idx in dp])


        #Dp space optmized O(n^3) space O(2n) we are going TOP-DONW 
        dp=grid[0]
        for r in range(1,N):
            next_dp=[float('inf')]*N
            for curr_c in range(N):
                for prev_c in range(N):
                    if prev_c!=curr_c:
                        next_dp[curr_c]=min(next_dp[curr_c],dp[prev_c]+grid[r][curr_c])
            dp=next_dp
        return min(dp)

        #recusion check min while taking it
        cache={} #O(n^3) space O(n^2)
        def helper(r,c):
            if r==N-1:
                return grid[r][c]
            if (r,c) in cache:
                return cache[(r,c)]
            val=float('inf')
            for next_col in range(N):
                if c!=next_col:
                    val=min(val,grid[r][c] +helper(r+1,next_col))
            cache[(r,c)]=val
            return val

        res=float('inf')
        for c in range(N):
            res=min(res,helper(0,c))
        return res
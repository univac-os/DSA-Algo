class Solution:
    def minSteps(self, n: int) -> int:
        #looks like pick no pick but here we can paste--> 1 operation or copy&paste --> 2 operation
        #we need min so dp 
        #we will have count of operation

        #top-down we need to get the factor 
        dp=[1000]*(n+1)
        dp[1]=0
        for i in range(1,n+1):
            for j in range(1,1+ (i//2)):
                if i%j==0:
                    #its factor
                    dp[i]=min(dp[i],dp[j]+i//j)
        return dp[n] 

        cache = {}
        def dfs(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000  # Use infinity to signify an invalid path
            
            if (count, paste) in cache:
                return cache[(count, paste)]  
            #Paste the current clipboard content
            paste_option = 1 + dfs(count + paste, paste)
            #Copy all and then paste (2 operations: copy + paste)
            copy_paste_option = 2 + dfs(count + count, count)
            
            cache[(count, paste)] = min(paste_option, copy_paste_option)
            return cache[(count, paste)]
        
        if n == 1:
            return 0
        # Start with 1 character on the board and 1 character in the clipboard
        return 1 + dfs(1, 1)

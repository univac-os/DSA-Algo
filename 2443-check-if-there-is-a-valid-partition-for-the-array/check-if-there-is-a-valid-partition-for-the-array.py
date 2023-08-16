class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        #edit distance
        #memory optimized we need only 3 value to check bottom up approach
        two=nums[-1]==nums[-2] #base case
        if len(nums)==2:
            return two
        three=(nums[-1]==nums[-2]==nums[-3]) or (nums[-3]+1==nums[-2]==nums[-1]-1)
        dp=[three,two,False]#inital value i+2 i+3 base
        for i in range(len(nums) -4,-1,-1):
            curr=(nums[i]==nums[i+1] )and dp[1]
            curr=curr or ((nums[i]==nums[i+1]==nums[i+2]) or (nums[i]+1==nums[i+1]==nums[i+2]-1) ) and dp[2]
            dp=[curr,dp[0],dp[1]]
        
        return dp[0]
        dp={}
        def dfs(i): #O(n)
            if i==len(nums):
                return True
            if i in dp:
                return dp[i]
            res=False
            if i+1<=len(nums)-1 and nums[i]==nums[i+1]:
                res=dfs(i+2)
            if i+2<=len(nums)-1:
                if (nums[i]==nums[i+1]==nums[i+2]) or (nums[i]+1==nums[i+1]==nums[i+2]-1):
                #if (sum(nums[i:i+3])//nums[i]==3) or (2*nums[i+1]==nums[i]+nums[i+2]):
                    res=res or dfs(i+3)
            dp[i]=res
            return dp[i]
        return dfs(0)

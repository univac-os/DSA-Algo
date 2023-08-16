class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        #edit distance
        dp={}
        def dfs(i):
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

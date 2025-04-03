class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        take not take we want sum/2 
        """
        total=sum(nums)
        if total%2:return False
        target=total//2
        n=len(nums)
        # dp=[[False]*(target+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=True
        
        # for i in range(1, n + 1):  # Start from 1 since dp[0][...] is base case
        #     for t in range(1, target + 1):
        #         dp[i][t] = dp[i - 1][t]  # Not taking nums[i-1]

        #         if t >= nums[i - 1]:  # Fixing the indexing issue
        #             dp[i][t] = dp[i][t] or dp[i - 1][t - nums[i - 1]]
        # return dp[n][target]
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for t in range(target, num - 1, -1):  # Iterate backwards to prevent reuse
                dp[t] = dp[t] or dp[t - num]

        return dp[target]

    
        dp={}
        def rec(i,count):
            if i>=len(nums):
                if count==0:return True
                return False
            if (i,count) in dp:
                return dp[(i,count)]
            nottake=rec(i+1,count)
            take=False
            if count>=nums[i]:
                if rec(i+1,count-nums[i]):
                    take=True

            dp[(i,count)]=take or nottake
            return dp[(i,count)]

        return rec(0,total//2)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #2. greedy  assume we need to reach goal so check from end can we reach there
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal: #from that point we can reach so go back and check
                goal=i
        return True if goal ==0 else False#we can reach from start

        #1.dp check whether we can go from that position or not
        #memo
        n=len(nums)
        dp={}
        def dfs(i):
            if i==n-1:
                return True
            if nums[i]==0:
                return False
            if i in dp:
                return dp[i]
            for j in range(i+1,min(i+nums[i],n-1) +1):
                if dfs(j):
                    dp[j]=True
                    return True
            
            return False
        return dfs(0)
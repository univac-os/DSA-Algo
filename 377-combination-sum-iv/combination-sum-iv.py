class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #for loop to check with every number
        #bottom up
        dp={0:1} #base case
        for total in range(1,target+1):
            dp[total]=0
            for n in nums:
                dp[total]+=dp.get(total-n,0)
        
        return dp[total]

        dp={}
        def dfs(t):
            if t==0:
                return 1
            if t<0:
                return 0
            if t in dp:
                return dp[t]
            res=0
            for n in nums:
                res+=dfs(t-n)
            dp[t]=res

            return dp[t]
        
        return dfs(target)


class Solution:
    def rob(self, nums: List[int]) -> int:
        #better we can use 2 var to check as all nums are + we need to take val and go on
        rob1,rob2=0,0
        #[rob1,rob2 ,n ,n+1]
        for i in range(len(nums)):
            tmp=max(nums[i]+rob1,rob2)
            rob1=rob2
            rob2=tmp
        return rob2        
        #pick not pick O(2^n)
        cache={} 
        def dfs(n):
            if n>=len(nums):
                return 0
            if n in cache:
                return cache[n]
            #not pick
            notPick=dfs(n+1)
            #pick
            pick=nums[n]+dfs(n+2)
            cache[n]=max(pick,notPick)
            return cache[n]

        return dfs(0)
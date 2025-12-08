class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        pick or not pick but if divisble why not pick 2 6 8 so here at 6 we wont pick 8 but at 2 we will pick 6 Greedy (less val easy to divisible)
        so we will take and check O(n2)
        """
        nums.sort()

        dp=[[n] for n in nums]
        res=[]
        for i in reversed(range(len(nums))):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    tmp=[nums[i]]+dp[j]
                    if len(tmp)>len(dp[i]):
                        dp[i]=tmp
            res=dp[i] if len(dp[i])>len(res) else res
        return res
        cache={}#store the index
        def dfs(i):
            if i==len(nums):
                return []
            if i in cache: return cache[i]

            res=[nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    tmp=[nums[i]]+dfs(j) #taking next greater val and check with next values
                    if len(tmp)>len(res):
                        res=tmp
            cache[i]=res
            return res

        res=[]
        for i in range(len(nums)):
            tmp=dfs(i)
            if len(res)<len(tmp):
                res=tmp
        return res
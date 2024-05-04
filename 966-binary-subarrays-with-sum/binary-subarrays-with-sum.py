class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #o(n2) check with each one
        #sliding window O(n) if goal is 0 then problem
        #set of goal -set of (goal-1)=exact goal number
        def helper(x):
            if x<0:
                return 0
            res=0
            l,curr_sum=0,0
            for r in range(len(nums)):
                curr_sum+=nums[r]
                while curr_sum>x:
                    curr_sum-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        
        return helper(goal)-helper(goal-1)
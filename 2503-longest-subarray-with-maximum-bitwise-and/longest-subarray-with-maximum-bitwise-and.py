class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #we need max value 1st
        #then check the continuous of this max number O(n+n)
        target=max(nums)
        res,curr=1,0
        for n in nums:
            if n==target:
                curr+=1
            else:
                curr=0
            res=max(res,curr)
        return res
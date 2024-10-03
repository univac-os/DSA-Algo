class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #prefix sum
        #looking at example you need smallest subarray so we need to remainder at index to be stored, so that we can get len of sub array
        remainder=sum(nums)%p
        curr_sum=0
        res=len(nums)
        remind_idx={0:-1}#base case
        if remainder==0:return 0
        for idx,n in enumerate(nums):
            #prefix sum+ remainder=curr_sum
            #so prefix sum=curr_sum-remainder
            #% by p --> prefix sum%p =curr_sum%p -0 
            curr_sum=(curr_sum+n)%p
            prefix_mod=(curr_sum-remainder +p)%p #if remainder is more than curr_sum so -ve rem
            #now check %
            if prefix_mod in remind_idx:
                res=min(res,idx-remind_idx[prefix_mod])
                
            remind_idx[curr_sum]=idx

        return -1 if res ==len(nums) else res
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #sliding window 
        #we need subarray moving r till end get the subarray
        #so take count of subarray
        #WHY count if taking the value and its within the product so indivdual it is also valid
        res=0
        l=0
        product=1
        for r in range(len(nums)):
            product*=nums[r]
            while l<=r and product >=k:
                #move l
                product/=nums[l]
                l+=1
            res+=(r-l+1)
        return res
        
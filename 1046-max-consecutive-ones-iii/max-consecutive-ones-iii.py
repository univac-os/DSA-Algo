class Solution:
    def longestOnes(self,nums, k)->int:
        # slinding window O(n)
        max_l,r=0,0
        l,zeros=0,0
        while (r<len(nums)):
            if nums[r]==0:
                zeros+=1
            
            if zeros>k:
                #shrink the window
                if (nums[l]==0):zeros-=1
                l+=1
            if zeros<=k:
                max_l=max(max_l,r-l+1)
            r+=1
        return max_l


        
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        prefix sum but 2 1 4 3 5 2 1 last 2,1 can form subarray
        so slinding window O(n)
        """
        res,total=0,0
        l=0
        for r in range(len(nums)):
            total+=nums[r]
            while l<=r and total*(r-l+1)>=k:
                total-=nums[l]#shrink the window
                l+=1
            res+=r-l+1
        return res
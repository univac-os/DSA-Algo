class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        here we can make interval and [x-k,x+k] and do merge interval
        better we check a+k , b-k if these are merging both can taken
        b-k - (a+k)--> b-a -2k--> b-a 
        and sliding window O(n)
        """
        nums.sort() # we want subseq not continuous subseq
        res=0
        l=0
        for r in range(len(nums)):
            while nums[r]-nums[l]> 2*k:#no need to check r-l as 0>2*k
                l+=1
            res=max(res,r-l+1)#include both side
        return res
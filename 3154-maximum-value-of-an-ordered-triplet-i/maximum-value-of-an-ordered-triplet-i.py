class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        you should not sort the value looking at example [1,2,3]
        so we want i--> maxi j-->mini k-->maxi
        instead of O(n3)we can go through nums and if we find any max value till now we go and find j and k 
        """
        res=0
        n=len(nums)
        left=nums[0]
        middle=nums[1]
        for j in range(1,n):
            if nums[j]>left:
                left=nums[j]
            for k in range(j+1,n):
                res=max(res,(left -nums[j])*nums[k])
        return res


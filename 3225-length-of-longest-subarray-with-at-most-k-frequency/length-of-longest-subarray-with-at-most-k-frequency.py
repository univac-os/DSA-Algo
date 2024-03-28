class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res=0
        char_count=defaultdict(int)
        l=0
        for r in range(len(nums)):
            char_count[nums[r]]+=1
            while char_count[nums[r]]>k:
                #move window
                char_count[nums[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        ans will be 1 to len(nums)+1 so check the val is present O(n)
        """
        nums=set(nums)
        res=len(nums)+1
        for i in range(1,len(nums)+2):
            if i not in nums:
                return i
        return res
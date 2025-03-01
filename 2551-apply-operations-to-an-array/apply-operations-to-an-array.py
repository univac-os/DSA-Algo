class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        #take non zero number and add to result array and give it
        res=[0]*len(nums)
        i=0
        for j in range(len(nums)):
            if nums[j]:
                res[i]=nums[j]
                i+=1
        return res
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        we can have 3 lists and add the element based on condition and combine them O(N) space is O(N)
        wihtout space 2ptr start from start take all element from start and similar from back to maintain order
        """
        res=[pivot]*len(nums)
        idx=0
        for i in range(len(nums)):
            if nums[i]<pivot:
                res[idx]=nums[i]
                idx+=1
        idx=len(nums)-1
        for i in reversed(range(len(nums))):
            if nums[i]>pivot:
                res[idx]=nums[i]
                idx-=1
        return res
            
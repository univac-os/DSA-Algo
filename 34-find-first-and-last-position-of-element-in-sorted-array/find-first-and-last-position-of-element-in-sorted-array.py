class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums,target, True)
        right = self.binSearch(nums,target, False)
        return [left, right]

    # leftBias -- True to get the left-most value, False to get the right-most value
    def binSearch(self, nums, target,leftBias):
        l,r=0,len(nums)-1
        idx = -1
        while l <= r:
            m=(l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                idx = m
                if leftBias:
                    # move left
                    r = m - 1
                else:
                    # move right
                    l = m + 1
        return idx

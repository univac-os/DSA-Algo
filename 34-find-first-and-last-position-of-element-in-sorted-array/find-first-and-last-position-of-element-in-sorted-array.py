class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #1. we can use same find left most value and for right target is +1
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:#check mid is at start or left side is same
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:#check mid is last or mid+1 value is same 
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
        
        def RightBinSearch(nums,target):
            l,r=0,len(nums)-1
            while l<r:
                m=(l+r)//2
                if nums[m]>target:
                    r=m-1
                else: #nums[m]<=target
                    l=m
            return l
        left=LeftBinSearch(nums,target)
        right=RightBinSearch(nums,target)
        return [left,right]
    
    #2. O(logn +logn)
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

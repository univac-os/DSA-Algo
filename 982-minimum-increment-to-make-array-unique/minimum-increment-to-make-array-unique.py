class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #we can use counting sort but its not useful as O(n+max(nums)) because say 
        #nums=[2,2] the we need [2,3]
        count=Counter(nums)
        res=0
        for i in range(len(nums)+max(nums)):
            if count[i]>1:
                extra=count[i]-1
                res+=extra
                count[i+1]+=extra
        return res

        #we need unique so sort value and make the array increasing order
        # 4 3 are 2 nums so here we need increase 3 to 5(diff of 4-3 +1)
        nums.sort()
        res=0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                res+=1+ nums[i-1]-nums[i]
                nums[i]=nums[i-1]+1
        return res
        
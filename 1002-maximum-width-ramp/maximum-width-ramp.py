class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        we wwant right>=left so start from right get (min,max) index till that point
        and check from last to first
        looking at this we can see we only need max value as given num on left < max till that index
        once e get max value we can check from start as we know there are max value at every index
        '''
        max_right=[0]*(len(nums))
        max_right[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            max_right[i]=max(max_right[i+1],nums[i])
        
        #now check from l to r based on this max_right 
        res,l=0,0
        for r in range(len(nums)):
            while nums[l]>max_right[r]: #we can find max value for this index
                l+=1
            res=max(res,r-l)
        return res
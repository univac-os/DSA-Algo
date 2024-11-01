class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        '''
        draw graph --> does not help
        check one side of mountain LIS(longest increasing subseq)
        check another side LDS from reverse its LIS
        we got at pivot mountains both side 
        so n-LIS-LDS +1 (+1 as we have consider that pivot into subseq or we are - in both so add 1) O(n2 +n2 +n)
        '''
        N=len(nums)
        LIS=[1]*N
        for i in range(N):
            for j in range(i):
                if nums[j]<nums[i]:
                    LIS[i]=max(LIS[i],LIS[j]+1)
        
        LDS=[1]*N
        for i in reversed(range(N)):
            for j in range(i+1,N):
                if nums[i]>nums[j]:
                    LDS[i]=max(LDS[i],LDS[j]+1)
        
        #check for each point
        res=N
        for i in range(1,N-1):
            if LIS[i]>1 and LDS[i]>1:
                res=min(res,N-(LIS[i]+LDS[i]-1))
        return res

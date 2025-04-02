class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        l=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    temp=l[j]+1
                    l[i]=max(temp,l[i])
                
        return max(l)
        
        dp={}
        def rec(i,prev_idx):
            if i>=len(nums):
                return 0
            if (i,prev_idx) in dp:
                return dp[(i,prev_idx)]
            nottake =0+rec(i+1,prev_idx)
            take=0
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                take=1+rec(i+1,i)
            dp[(i,prev_idx)]=max(nottake,take)
            return dp[(i,prev_idx)]
        return rec(0,-1)
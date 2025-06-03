class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        draw line between the nums so where 
        prefix sum and get min diff among all is less and take max value from it
        draw ,not draw each point 
        """
        prefix_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        cache={}
        def dfs(i,cuts):
            if cuts==1:
                #take all remaining 
                return prefix_sum[len(nums)]-prefix_sum[i]
            #left side ,right side of cut
            if (i,cuts) in cache:return cache[(i,cuts)]
            max_res=float('inf')
            for j in range(i+1,len(nums)-cuts+2):
                left=prefix_sum[j]-prefix_sum[i]
                right=dfs(j,cuts-1)
                curr_max=max(left,right)
                max_res=min(max_res,curr_max)
                if left>max_res:break
            cache[(i,cuts)]=max_res
            return max_res
                
        return dfs(0,k)

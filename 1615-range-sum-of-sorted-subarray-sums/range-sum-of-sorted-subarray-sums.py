class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        #find sub array of sum and sort it and get the required range O(n2 + n^2logn^2 -- for subarray list)
        sub_array_sum=[]
        Mod=10**9+7
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum=(curr_sum+nums[j])%Mod
                sub_array_sum.append(curr_sum)
        
        sub_array_sum.sort()
        return sum(sub_array_sum[left-1:right])%Mod
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        we need count of 0 in both array and sum of both array
        we take max sum array and make it min after append the val in place of 0
        what val we will add 1 inplace of 0 
        """
        s1,s2=sum(nums1),sum(nums2)
        c1,c2=nums1.count(0),nums2.count(0)
        #how we have count of 0 and sums now
        #assume we have added 1 in place of 0 and check the sum if diff is there check how many 0 are there to adjust it
        min_s1,min_s2=s1+c1,s2+c2
        if (c1==0 and min_s1<min_s2) or (c2==0 and min_s1>min_s2): return -1
        return max(min_s1,min_s2)
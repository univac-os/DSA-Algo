class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        DP include exclude type O(n2)
        but better we know answer will be from [min,max] of array in between these value
        so binary search between these value O(nlogn)
        BUT say we got a num which is not in array,if it satisfy we moving inside 
        so we will get a num present in array
        """
        def is_valid(m):
            #include exclude
            count=0
            i=0
            while i<len(nums):
                if nums[i]<=m:
                    count+=1
                    i+=2
                else:
                    i+=1
                if count==k:
                    return True
            return False

        l,r=min(nums),max(nums)
        res=0
        while l<=r:
            m=(l+r)//2
            if is_valid(m):
                res=m
                r=m-1 #greedy find minimum value
            else:
                l=m+1
        return res
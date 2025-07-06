class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        O(n2) find all subarray,we want min and max in subarray and consecutive
        https://leetcode.com/problems/sum-of-subarray-minimums/description/
        so we need to find the subarray where the num is minimum in it then total we can get subarray
        so we need monotonic stack inc/dec to find the next greater/lesser element 
        so res=sum(maxi)-sum(mini) where num in present in subarray
        """
        n,res=len(nums),0
        stack=[] #(idx)
        #find num in subarray where it is minimum
        for right in range(n+1):
            while stack and (right==n or nums[stack[-1]]>=nums[right]):
                #pop it and calculate the min the num present in subarry
                mid=stack.pop()
                left=stack[-1] if stack else -1 #start point
                res-=nums[mid]*(mid-left)*(right-mid)
            stack.append(right)

        stack.clear()
        #find num in subarray where it is maximum
        for right in range(n+1):
            while stack and (right==n or nums[stack[-1]]<=nums[right]):
                #pop it and calculate the max the num present in subarray
                mid=stack.pop()
                left=stack[-1] if stack else -1
                res+=nums[mid]*(mid-left)*(right-mid)
            stack.append(right)
        
        return res
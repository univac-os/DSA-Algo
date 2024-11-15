class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        stack to getting increasing order --> okay but we need to remove middle part how
        so first get incresing order from backside
        now from front we will check with this backside 
        so we will reduce backside sorted protion with frontside so that middle part is gone O(n)
        """
        #increasing backside
        N=len(arr)
        r=N-1
        while r>0 and arr[r-1]<=arr[r]:
            r-=1
        res=r #get the ptr of start of backside increasing order 
        l=0
        #check with frontside and reduce backside sub array
        while l<r:
            while r<N and arr[l]>arr[r]:
                r+=1
            res=min(res,r-l-1)
            if arr[l]>arr[l+1]:
                break
            l+=1
        return res
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        stack to getting increasing order --> okay but we need to remove middle part how
        so first get incresing order from backside
        now from front we will check with this backside 
        so we will reduce backside sorted protion with frontside so that middle part is gone O(n)
        """
        #get increasing backside
        N=len(arr)
        r=N-1
        while r>0 and arr[r-1]<=arr[r]:
            r-=1
        res=r #get starting index of backside
        l=0
        #Now check frontside and backside and reduce backside subarray so that we will get middle part
        while l<r:
            #to remove middle part
            while r<N and arr[l]>arr[r]:
                r+=1
            res=min(res,r-l-1)
            #check frontside
            if arr[l]>arr[l+1]:
                break
            l+=1
        return res
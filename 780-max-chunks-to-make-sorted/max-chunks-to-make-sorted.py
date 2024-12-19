class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        see condition number are in range[0,n-1]
        and we want sorted so final arr should be [0,1,2,3...n-1]
        say we got 3 at start ,to sort this we need to wait minimum till index 4(3+1)
        assume arr is like 3 0 2 1 4 5 we make partition 3 0 2 1 | 4 | 5
        at 4 and 5 we will check index and value same so make partition greedy
        PREFIX check large value 
        """
        partition=0
        curr_Max=-1
        for idx,n in enumerate(arr):
            curr_Max=max(n,curr_Max)
            if curr_Max==idx:
                partition+=1
        return partition
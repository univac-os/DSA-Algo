class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        sliding window to get subarray but we want smallest subarray so use min heap to store
        prefix sum --> to know the addition of numbers
        this prefix sum will get you knew which are not required to consider 
        O(n logn) --> logn to pop/add in min heap
        """
        res=float('inf')
        min_heap=[] #(prefix_sum,end_ptr)
        curr_sum=0
        for r in range(len(nums)):
            curr_sum+=nums[r]
            if curr_sum >=k:
                res=min(res,r+1) 
            #check from heap
            while min_heap and curr_sum -min_heap[0][0]>=k:
                _,end=heapq.heappop(min_heap)
                res=min(res,r-end) #we will are not taking end ptr in sub array
            heapq.heappush(min_heap,(curr_sum,r))


        return -1 if res==float('inf') else res
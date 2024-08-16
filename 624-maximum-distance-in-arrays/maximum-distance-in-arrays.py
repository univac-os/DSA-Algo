class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        #kadane algo type find curr min,max and find overall min,max 
        curr_min,curr_max=arrays[0][0],arrays[0][-1]
        res=0
        for i in range(1,len(arrays)):
            arr=arrays[i]
            res=max(res,arr[-1]-curr_min,curr_max-arr[0])
            
            #update min and max
            curr_min=min(curr_min,arr[0])
            curr_max=max(curr_max,arr[-1])  
        return res
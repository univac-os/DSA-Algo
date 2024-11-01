class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        #check with 2 list HOW--> 2 ptr and move min val ptr to next
        #similar to this we use ptr but we need min val on each go
        #HOW to get that min_heap O(logk)
        #so we store (val,idx_list,idx_element)
        k=len(nums)
        left=right=nums[0][0]
        min_heap=[]
        for i in range(k):
            num=nums[i][0]
            left=min(left,num)
            right=max(right,num)
            heapq.heappush(min_heap,(num,i,0)) # val, idx of list ,idx of element
        
        #now we have heap so get min distance interval by moving ptr 
        res=[left,right]
        while True:
            n,idxL,idxE=heapq.heappop(min_heap)
            idxE+=1#move ptr to next position
            if idxE==len(nums[idxL]):#if end of array we got value
                return res

            nxt_val=nums[idxL][idxE] #get next value and check min interval
            heapq.heappush(min_heap,(nxt_val,idxL,idxE))
            right=max(right,nxt_val) #check next val is max or not
            left=min_heap[0][0] #get min val
            if right-left<res[1]-res[0]:
                res=[left,right]
        
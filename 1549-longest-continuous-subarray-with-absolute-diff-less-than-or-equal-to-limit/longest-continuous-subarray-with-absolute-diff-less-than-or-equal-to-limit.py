class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 10 1 2 4 7 2 limit =5 
        # 10 1 which i need to ignore 10 or 1 slinding window does not work here
        # we can take 2 heaps with min val in 1 heap and max val in another heap
        #based on diff according to limit we take to heap O(nlogn)
        #but here we are considering max and min val are present in solution which is not correct
        # we want contious sub array so slinding window so we need check min and max value of the heap ,So we can get len og sub array

        #BETTER WE CAN TAKE queue in inceasing and decreasing order and check limit and remove them
        max_q,min_q=deque(),deque()
        l,res=0,0
        for r in range(len(nums)):
            #make max queue in decreasing order
            while max_q and max_q[-1]<nums[r]:
                max_q.pop()#remove that element
            max_q.append(nums[r])
            #similar min queu in increasing order
            while min_q and min_q[-1]>nums[r]:
                min_q.pop()#remove that element
            min_q.append(nums[r])
            #now we made queue in increase & decreas order but what about continous 
            while max_q[0]-min_q[0]>limit:
                #remove the element to reduce the gap
                if max_q[0]==nums[l]:
                    max_q.popleft()
                if min_q[0]==nums[l]:
                    min_q.popleft()
                l+=1
            res=max(res,r-l+1)
        return res
        max_h,min_h=[],[]
        l=0
        res=0
        for r in range(len(nums)):
            heapq.heappush(max_h,(-1*nums[r],r)) #(val,idx)
            heapq.heappush(min_h,(nums[r],r))
            #we will check limit and remove from heap and get the res
            while (-1*max_h[0][0] - min_h[0][0])>limit:
                #remove from which heap 
                l=min(max_h[0][1],min_h[0][1])+ 1 #removed that element from window
                
                #check that element in heap range as we want continous sub array
                while max_h[0][1]<l:
                    heapq.heappop(max_h)
                while min_h[0][1]<l:
                    heapq.heappop(min_h)
                
            res=max(res,r-l+1)
        return res

        

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums.sort()
        #return nums[-k]
        #max heap
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)  
        kth_largest = None
        for _ in range(k):
            kth_largest = -heapq.heappop(max_heap) 
    
        return kth_largest

        #we can use quick sort
        k=len(nums)-k

        def quickSelect(l,r):
            #select pivot as right most element
            pivot,p=nums[r],l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            
            # we need to exchange p with privot
            nums[p],nums[r]=nums[r],nums[p]

            #check left or right
            if p>k:
                #left side
                return quickSelect(l,p-1)
            elif p<k:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)
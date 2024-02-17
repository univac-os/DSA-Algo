class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #bucket sort build -hashmap O(n) and remove from bucket O(n)
        freq=Counter(arr)
        freq_list=[0]*(len(arr)+1)
        for f in freq.values():
            #take freq of each number and update in index of freq_list
            freq_list[f]+=1
        res=len(freq)
        for count in range(1,len(freq_list)):
            remove=freq_list[count]
            #remove complete set or each one
            if k>=count*remove:
                #remove complete set
                k-=count*remove
                res-=remove
            else:
                #each element but which one say we have k=3 arr=[5,3,1] we want [5,0,1] not [3,3,1]
                remove=k//count #leave bigger value
                res-=remove
                break 
        return res

        
        # MIN-HEAP - build heap--O(n) and pop element O(logn)
        freq = Counter(arr)
        minHeap=list(freq.values())
        heapq.heapify(minHeap)
        res=len(minHeap)
        while k>0 and minHeap:#if k>len(heap) then invalid
            count=heapq.heappop(minHeap)
            if k>=count:#remove all occurance of that number
                k-=count
                res -=1
        return res

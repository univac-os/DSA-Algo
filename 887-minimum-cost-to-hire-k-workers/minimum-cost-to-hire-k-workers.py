class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        #get ratios--wage/quality and sort by it
        #minimum val is needed so quality need be less in our ans
        #so maxheap to check quality
        ans=float('inf')
        pairs=[] #(ratio,quality)
        for i in range(len(wage)):
            pairs.append((wage[i]/quality[i],quality[i]))
        pairs.sort(key=lambda p:p[0]) #sort by ratio
        maxHeap=[]# for quality
        total_quality=0
        for rate,q in pairs:
            #1.take quality and push to maxheap
            #2.check with k and get min res
            #if maxheap is more than k ,remove the largest quality in it
            heapq.heappush(maxHeap,-q)
            total_quality+=q
            if len(maxHeap)>K:
                #remove 
                total_quality +=heapq.heappop(maxHeap)
            if len(maxHeap)==K:
                ans=min(ans,total_quality*rate)
        return ans
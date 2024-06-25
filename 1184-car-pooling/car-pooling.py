class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #looks scheduling problem sort by start time ,check capacity and 
        #remove capacity when least end point is trigger
        # to check this end point use min HEAP O(nlogn + nlogn--heap)
        trips.sort(key=lambda t:t[1])
        minH=[] #(end,capacity)
        currCapa=0
        for t in trips:
            cap,start,end=t
            #check if we can reduce capacity
            while minH and minH[0][0]<=start:
                #ride is over
                currCapa-=minH[0][1]
                heapq.heappop(minH)

            currCapa+=cap
            if currCapa>capacity:
                return False
            heapq.heappush(minH,(end,cap))
        
        return True
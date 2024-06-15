class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #we want to have min capital and max profit in given k 
        #for min cap--minheap 
        #for max profit -- maxheap
        maxProfit=[]
        minCapital=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            #check c from min Capital with w 
            while minCapital and minCapital[0][0]<=w:
                #add to maxPRofit heap and take max value
                c,p=heapq.heappop(minCapital)
                heapq.heappush(maxProfit,-p)
            if not maxProfit:
                #before k comes maxprofit is empty then we cant do anything
                break
            w+=-1* heapq.heappop(maxProfit)
        return w
            
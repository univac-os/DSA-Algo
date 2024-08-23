class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #hashset take a num that min in set ,remove it and add element num*2,num*3,num*5 O(n2)
        #here we need min num so use minheap O(nlogn)
        minH=[1]
        visit=set()
        factors=[2,3,5]
        for i in range(n):
            minV=heapq.heappop(minH)
            if i==n-1:
                return minV
            
            for f in factors:
                if minV*f not in visit:
                    heapq.heappush(minH,minV*f)
                    visit.add(minV*f)
        
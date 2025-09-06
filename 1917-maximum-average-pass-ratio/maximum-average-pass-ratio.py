class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        avg of 1 adding extra student not useful
        nr/dr nr<dr and extra increases the overal val so we need to check where we can get better 
        at each time we give 1 to everyone and check improvement and finalize it and do it next time O(n*k)
        nr+1/dr+1 -nr/dr is delta which should be more GREEDY
        """
        def delta(nr,dr):
            return ((nr+1)/(dr+1)) -(nr/dr)
        max_h=[]
        #inital with +1 
        for nr,dr in classes:
            heapq.heappush(max_h,(-delta(nr,dr),nr,dr)) # delta
        
        i=1
        while i<=extraStudents:
            _,nr,dr =heapq.heappop(max_h) #we got better improvement so do it next time
            nr+=1
            dr+=1
            heapq.heappush(max_h,(-delta(nr,dr),nr,dr))
            i+=1
        
        res=0
        while max_h:
            _,nr,dr=heapq.heappop(max_h)
            res+=(nr/dr)
        return res/len(classes)




        

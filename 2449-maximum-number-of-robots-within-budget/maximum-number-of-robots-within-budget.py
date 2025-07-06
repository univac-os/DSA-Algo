class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        """
        max()+k*sum()<=Budget so we want consective so slinding window but finding max will be
        difficult as we need to get everytime in window,so having to get it it will be O(window)
        how can we do this? queue we maintain decreasing queue so if l==max then we get next number 
        """
        n=len(chargeTimes)
        l=0
        wind,res=0,0
        max_q=deque()#decreasing mono queue
        for r in range(n):
            wind+=runningCosts[r]
            #adjust the queue
            while max_q and chargeTimes[r]>max_q[-1]:
                max_q.pop()
            max_q.append(chargeTimes[r])
            k=r-l+1
            total=max_q[0] + k*wind
            #check with budget 
            while total>budget:
                wind-=runningCosts[l]
                if chargeTimes[l]==max_q[0]:
                    max_q.popleft()
                
                l+=1
                k=r-l+1
                total=max_q[0]+k*wind if k>0 else 0
            res=max(res,k)
                 
        return res
        
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        the task will be available after t_now+space 
        so we can use hashmap to get the details O(n)
        """
        nxt_t=defaultdict(int)
        time=0
        for t in tasks:
            time+=1
            if nxt_t[t]>time:
                time=nxt_t[t]
            nxt_t[t]=time+space+1#next available
        return time

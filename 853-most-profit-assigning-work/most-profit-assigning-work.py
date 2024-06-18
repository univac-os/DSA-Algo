class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #greedy -- take best job so we get best profit
        # sort worker and difficulty and get the value O(nlogn. +mlogm) -2 ptr
        #instead of sort worker ,sort difficulty and bineay search on difficulty array O(nlogn)
        #max heap and start from reverse of worker(sorted) and get the value O(nlogn+ mlogm)
        Job=namedtuple('WorkJob',['diff','pro'])
        worker.sort()
        work_queue=deque(sorted(list(Job(d,p) for d,p in zip(difficulty,profit) ),key=lambda x:x[0] ) ) 
        res=0
        best=0
        for w in worker:
            while work_queue and work_queue[0].diff<=w:
                best=max(best,work_queue[0].pro)
                work_queue.popleft()
            res+=best
        return res

        
        
        worker.sort(reverse=True)
        res=0
        maxH=[(-p,d) for d,p in zip(difficulty,profit)] # we want some profit
        heapq.heapify(maxH)
        for w in worker:
            while maxH and maxH[0][1]>w:
                heapq.heappop(maxH)
            if not maxH:
                break
            res+=-1*maxH[0][0]

        return res

         
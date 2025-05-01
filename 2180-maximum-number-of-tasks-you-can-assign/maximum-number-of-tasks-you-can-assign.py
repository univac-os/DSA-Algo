class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        greedy find task which is closes to worker so use Binary search
        say there 5 tasks i want this to finish so if i assign this to 5 strong workers can be done means
        weaker worker can do it as well SO more tasks can be done
        so we take 0..k tasks and check with -k workers if yes then we check k+x tasks with -k+x workers
        so if we can't do the use pill say worker =5 strength=5 and tasks are 5 9 12 14 15 
        so using pill worker can do task anything <=10 so 5 ,9 so i will use for 9 task GREEDY
        """
        def check(k):
            p=pills
            ws=SortedList(workers[-k:])
            for i in range(k-1,-1,-1):#large to small task
                if ws[-1]>=tasks[i]:
                    ws.pop()# use worker for that task
                else:
                    #check with using pills
                    if p==0:return False
                    idx=ws.bisect_left(tasks[i]-strength) # get which tasks we can remove using strength 
                    if idx==len(ws):return False
                    ws.pop(idx)#remove that task
                    p-=1
            return True


        n,m=len(tasks),len(workers)
        tasks.sort()
        workers.sort()

        l,r=0,min(n,m)
        res=0
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m # task can be done
                l=m+1
            else:
                r=m-1
        return res



class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #looks like graph check incoming =n-1 and outgoing=0
        #so we can use delta (incoming-outgoing=n-1-0)
        delta=defaultdict(int)
        for src,dest in trust:
            delta[src] -=1 #outgoing
            delta[dest] +=1 #incoming
        for i in range(1,n+1):
            if delta[i]==n-1:
                return i
        return -1
        
class Solution:
    def partitionString(self, s: str) -> int:
        #greedy
        currSet=set()
        res=1#init we take 1 partition
        for c in s:
            if c in currSet:
                res+=1
                currSet=set()#empty it
            currSet.add(c)
        
        return res
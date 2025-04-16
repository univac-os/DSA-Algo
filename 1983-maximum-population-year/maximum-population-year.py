class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        think as line we want how many lines are intersecting at which point
        so here point need to birth year (seeing examples)
        """
        n=2050-1950+1
        yr=[0]*n
        for l in logs:
            yr[l[0]-1950]+=1
            yr[l[1]-1950]-=1
        curr,maxi=0,0
        res=logs[0][0]
        for idx,y in enumerate(yr):
            curr+=y
            if curr>maxi:
                maxi=curr
                res=idx+1950
        return res




class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        left more right less we need to find the point 
        mono queue from both side NOT GOOD ? we are finding min/max here
        prefix the computation consective so prefix it
        """
        n=len(security)
        dec=[0]*n
        inc=[0]*n
        for i in range(1,n):
            if security[i]<=security[i-1]:
                dec[i]=dec[i-1]+1
        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                inc[i]=inc[i+1]+1
        
        #now check for each one
        res=[]
        print(inc,dec)
        for i in range(time,n-time):
            if min(inc[i],dec[i])>=time:
                res.append(i)
        return res
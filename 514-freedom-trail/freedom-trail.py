class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        #looks like dp -subproblem
        #which path need to take clockwise or anti clockwise -- get the len and go for next char
        cache={}
        def helper(r,k):
            if k==len(key):
                return 0 #got all chars
            if (r,k) in cache:
                return cache[(r,k)]
            res=float('inf')
            for idx,c in enumerate(ring):
                if c==key[k]:
                    min_dist=min(abs(r-idx), #straing path clockwise
                    len(ring)-abs(r-idx)) #reverse path. anti clockwise
                    res=min(res,min_dist +1 +helper(idx,k+1))
            cache[(r,k)]=res
            return res
        
        return helper(0,0)
        
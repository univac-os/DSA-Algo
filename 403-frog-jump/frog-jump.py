class Solution:
    def canCross(self, stones: List[int]) -> bool:
        #inital jump is 1
        #1.we want map of number and index
        hm={}
        for i in range(len(stones)):
            hm[stones[i]]=i

        dp={}
        def dfs(val,jump):
            if val not in hm:
                return False
            if val==stones[-1]:# last value
                return True
            
            if (val,jump) in dp:
                return dp[(val,jump)]

            for j in [jump-1,jump,jump+1]:
                #take jump greater than 0
                if val+j>val and dfs(val+j,j):
                    dp[(val,jump)]=True
                    return dp[(val,jump)]
            
            dp[(val,jump)]=False
            return dp[(val,jump)]
        
        if stones[1]==1:
            return dfs(1,1)
        else:
            return False
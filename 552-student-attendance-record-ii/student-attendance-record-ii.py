class Solution:
    def checkRecord(self, n: int) -> int:
        #looks dp we need to have state machine for L
        Mod=10**9+7
        cache=[[[-1]*3 for _ in range(2)]for _ in range(n+1)] # n a l
        def rec(n,absence,lates):
            if absence>=2 or lates>=3:
                return 0
            if n==0:
                return 1
            if cache[n][absence][lates]!=-1:
                return cache[n][absence][lates]
            count =rec(n-1,absence,0) # choose P so consecutive lates 0
            count=(count+rec(n-1,absence+1,0))%Mod #choose A so consecutive lates 0
            count=(count+rec(n-1,absence,lates+1))%Mod #choose L so consecutive lates are there
            cache[n][absence][lates]=count
            return count

        return rec(n,0,0)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #word break type
        n=len(s)
        words=set(dictionary)
        
        dp={}
        def dfs(i):
            if i==n:
                return 0#base case
            if i in dp:
                return dp[i]
            #not take
            res=1+dfs(i+1)
            for j in range(i,n):
                if s[i:j+1] in words:
                    #take 
                    res=min(res,dfs(j+1))
            dp[i]=res
            return dp[i]

        return dfs(0)
        
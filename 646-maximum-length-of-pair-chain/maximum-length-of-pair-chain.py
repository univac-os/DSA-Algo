class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #dp take not take
        pairs.sort()
        n=len(pairs)
        res=1
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if pairs[i][1]<pairs[j][0]:
                    dp[i]=max(dp[i],1+dp[j])
            res=max(res,dp[i])
        
        return res
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        #sub problem is there looks DP
        #start from back
        res=float('-inf')
        n=len(energy)
        dp=[0]*n
        for i in range(n-1,-1,-1):
            dp[i]=energy[i] + (dp[i+k] if i+k<n else 0)
            res=max(dp[i],res)
        return res
        
        
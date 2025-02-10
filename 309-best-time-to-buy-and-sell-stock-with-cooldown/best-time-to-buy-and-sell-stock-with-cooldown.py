class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        include/exclude O(2^n)
        caching O(n*2)
        """
        dp={}# (idx,buying)-->max value
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            #check if bought then 2 option sell or move to next
            if buying:
                buy=dfs(i+1,not buying) -prices[i]
                exclude=dfs(i+1,buying)
                dp[(i,buying)]=max(buy,exclude)
            #if sold  then move 2 steps forward
            else:
                sell=dfs(i+2,not buying) +prices[i]
                exclude=dfs(i+1,buying)
                dp[(i,buying)]=max(sell,exclude)
            
            return dp[(i,buying)]
                
        return dfs(0,True)
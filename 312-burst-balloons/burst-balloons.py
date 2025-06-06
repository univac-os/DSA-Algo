class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        take or not take at each step O(2^n) and cache O(n2)
        but if taken prev nums present as also need to considered
        so simple take ,not take wont work better ? window middle is removed
        removing extreme end at start is waste greedy say 9 3 1 5 2 7
        removing 1st 1 then 2 ,3 so ordering no give right always so
        take all posible l.. i...r  so 3 parts left side ,right side and middle
        so here we fix left and right and i changes in between them calculate O(n3)
        """
        nums=[1]+nums+[1]
        n=len(nums)
        #bottom up
        dp=[[0]*n for _ in range(n)]
        
        for l in range(n-2,-1,-1):
            for r in range(l+2,n):
                for i in range(l+1,r):
                    coins=nums[l]*nums[i]*nums[r]+dp[l][i]+dp[i][r]
                    dp[l][r]=max(dp[l][r],coins)
        return dp[0][n-1]


        cache={}
        def dfs(l,r):
            if l>=r:#here l and r are boundary not taking them
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            max_coins=0
            for i in range(l+1,r):
                coins=nums[l]*nums[i]*nums[r]+dfs(l,i)+dfs(i,r)
                max_coins=max(max_coins,coins)
            cache[(l,r)]=max_coins
            return max_coins
        return dfs(0,n-1)


        
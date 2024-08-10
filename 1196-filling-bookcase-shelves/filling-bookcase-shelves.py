class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        #greedy wont work similar to COIN CHANGE PROBLEM
        #we need to add books in same shelf or new row 
#DP     
        dp=[0]*(len(books)+1)
        for i in range(len(books)-1,-1,-1):
            remaining_width=shelfWidth
            max_ht=0
            dp[i]=float('inf')
            for j in range(i,len(books)):
                wd,ht=books[j]
                if remaining_width-wd<0:
                    break
                remaining_width-=wd
                max_ht=max(max_ht,ht)
                dp[i]=min( dp[i] , dp[j+1] + max_ht)

        return dp[0] 

        cache={}
        def dfs(i):
            if i==len(books):
                return 0 #base case
            if i in cache:
                cache[i]
            remaining_width=shelfWidth
            max_ht=0
            res=float('inf')
            for j in range(i,len(books)):
                #try to keep in same row
                wd,ht=books[j]
                if remaining_width-wd<0:
                    break 
                remaining_width -=wd
                max_ht=max(max_ht,ht)
                #now we can have option to add in new row
                res=min(res, max_ht + dfs(j+1) )#new row)
                cache[i]=res

            return cache[i]
        
        return dfs(0)
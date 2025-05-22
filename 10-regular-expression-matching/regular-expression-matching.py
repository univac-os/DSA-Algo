class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        take not take 
        if take jump +2 and again take ,not take O(2^n) and cache O(n2)
        """
        cache={}
        def dfs(i,j):
            if i>=len(s) and j>=len(p):
                return True # we can get matching
            if j>=len(p):return False #there are no char to match
            #if we came at end of i and there still char in j it will go to not take and return finally
            if (i,j) in cache:return cache[(i,j)]
            match= i<len(s) and (s[i]==p[j] or p[j]==".")
            if j+1<len(p) and p[j+1]=="*":
                #2 options #not take and take
                cache[(i,j)]=dfs(i,j+2) or (match and dfs(i+1,j))
                return cache[(i,j)]
            if match:
                cache[(i,j)]=dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)]=False
            return cache[(i,j)]

        return dfs(0,0)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dp ? take 1 ,* then how many we should take 1. no take 2. 1 take and repeat
        """
        n,m=len(s)-1,len(p)-1
        cache={}
        def dfs(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i <0 and j<0 :return True
            if j<0 :return False
            if i<0:
                return all(p[k]=="*" for k in range(j+1))
            res=False
            if s[i]==p[j] or p[j]=='?':
                res= dfs(i-1,j-1)
            elif p[j]=="*":
                res= dfs(i,j-1) or dfs(i-1,j)
            cache[(i,j)]=res
            return res

        return dfs(n,m)
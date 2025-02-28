class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        """
        LIS 2 options move one direction and backtrack
        we want supersubsequence so last element in dp array will the str
        """
        n,m=len(s1),len(s2)
        prev=[s2[j:] for j in range(m)]
        prev.append("") #bottom last element
        for i in reversed(range(n)):
            curr=[""]*m
            curr.append(s1[i:])
            for j in reversed(range(m)):
                if s1[i]==s2[j]:
                    curr[j]=s1[i]+prev[j+1] #diagonal
                else:
                    r1=s1[i]+prev[j]
                    r2=s2[j]+curr[j+1]
                    if len(r1)<=len(r2):
                        curr[j]=r1
                    else:
                        curr[j]=r2
            prev=curr
        return curr[0]

        cache={}
        def backtrack(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==len(s1):
                return s2[j:]
            if j==len(s2):
                return s1[i:]
            if s1[i]==s2[j]:
                return s1[i]+backtrack(i+1,j+1)
            r1=s1[i]+backtrack(i+1,j)
            r2=s2[j]+backtrack(i,j+1)
            if len(r1)<=len(r2):
                cache[(i,j)]=r1
                return r1
            else:
                cache[(i,j)]=r2
                return r2

        return backtrack(0,0)
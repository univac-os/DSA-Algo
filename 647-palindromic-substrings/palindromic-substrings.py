class Solution:
    def countSubstrings(self, s: str) -> int:
        #check left and right and move O(n^2)
        #check for odd len and even len pallindrom
        res=0
        def checkPal(l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                count+=1
            return count
            
        for i in range(len(s)):
            #odd len 
            res+=checkPal(i,i)
            #even len
            res+=checkPal(i,i+1)
        return res
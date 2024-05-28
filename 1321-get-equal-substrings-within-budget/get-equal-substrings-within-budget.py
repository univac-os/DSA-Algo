class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #check ith element and move on
        #sliding window--O(n)
        currCost=0
        res=0
        l=0
        for r in range(len(s)):
            currCost+=abs(ord(s[r])-ord(t[r]))
            while currCost> maxCost:
                #move window so reduce currCost
                currCost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            
            res=max(res,r-l+1)
        return res
        
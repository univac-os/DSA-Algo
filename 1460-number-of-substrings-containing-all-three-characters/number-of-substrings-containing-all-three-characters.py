class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        sliding window move till we have match find count by adding remaining and move the right prointer
        O(N) 2 ptr
        """
        l,res=0,0
        pre_a=[1,1,1]#a,b,c
        count=[0,0,0]
        for r in range(len(s)):
            count[ord(s[r])-ord('a')]+=1
            
            while all(count):
                #all check each value has some value similar count[0]>1 ,count[1]>1..
                res+=len(s)-r
                count[ord(s[l])-ord('a')]-=1
                l+=1
    
        return res
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum ( abs( ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1))
        res=0
        for i in range(len(s)-1):
            res+=abs(ord(s[i])-ord(s[i+1]))
        return res
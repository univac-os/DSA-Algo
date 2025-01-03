class Solution:
    def maxScore(self, s: str) -> int:
        #similar to prefix sum here we take 0 and 1 count and move the slider O(n)
        zeros=0
        ones=s.count('1') 
        res=0
        for i in range(len(s)-1):
            if s[i]=='0':
                zeros+=1
            else:
                ones-=1
            res=max(res,zeros+ones)
        return res

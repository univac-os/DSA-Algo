class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        #for dp we need to check only diff till k chars so 1D array is enough
        #so we need prev and curr array ? --not needed we are changing the char only once 
        dp=[0]*26
        for c in s:
            curr_char=ord(c)-ord('a')
            longest=1
            for prev_char in range(26):
                if abs(curr_char -prev_char)<=k:
                    longest=max(longest,1+dp[prev_char])
            dp[curr_char]=longest
        return max(dp)


        #subseq so think of dp can be use pick or not pick 
        cache={} #O(n*26)
        def helper(i,prev):
            if i==len(s):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            #not pick
            res=helper(i+1,prev)
            #pick
            if prev=="" or abs(ord(s[i])-ord(prev))<=k:
                res=max(res,1+helper(i+1,s[i]))
            
            cache[(i,prev)]=res
            return res
        
        return helper(0,"")

        
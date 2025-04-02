class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def rec(i):
            if i>=len(s):
                return True
            if i in dp:
                return dp[i]
            for w in wordDict:
                if i+len(w)<=len(s) and w ==s[i:i+len(w)]:
                    if rec(i+len(w)):
                        dp[i]=True
                        return True
            dp[i]=False
            return False
                  
        return rec(0)
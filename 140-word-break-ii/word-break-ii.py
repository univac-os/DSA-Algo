class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #include exclude we want list of word so backtrack to get another word-O(2^n)
        wordDict=set(wordDict)
        def backTrack(i):
            if i==len(s):
                res.append(' '.join(curr))
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    #include
                    curr.append(word)
                    backTrack(j+1)
                    #skip
                    curr.pop()
            
        curr=[]
        res=[]
        backTrack(0)
        return res        
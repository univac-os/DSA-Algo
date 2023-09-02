class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
class Trie:
    def __init__(self,words):
        self.root=TrieNode()
        for w in words:
            curr=self.root
            for c in w:
                if c not in curr.children:
                    #make new
                    curr.children[c]=TrieNode()
                curr=curr.children[c]#move there
            curr.is_word=True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #we can see only starting letter and decide whether it is present or not so use PREFIX TRIE
        n=len(s)
        words=set(dictionary)
        trie=Trie(dictionary).root
        
        dp={}
        def dfs(i): 
            if i==n:
                return 0#base case
            if i in dp:
                return dp[i]
            #not take
            res=1+dfs(i+1)
            
            curr=trie
            
            for j in range(i,n): #O(n)
                if s[j] not in curr.children:
                    break #we cant find taking this
                #present
                curr=curr.children[s[j]]
                if curr.is_word:
                    res=min(res,dfs(j+1))
            
            dp[i]=res
            return dp[i]

        return dfs(0) #O(n^3)

        #word break type
        n=len(s)
        words=set(dictionary)
        
        #bottom -up
        dp=[0]*(n+1) #base case is taken here
        for i in range(n-1,-1,-1):
            dp[i]=1+dp[i+1] #not take
            for j in range(i,n):
                if s[i:j+1] in words:
                    dp[i]=min(dp[i],dp[j+1])
        
        return dp[0]

        #top-down
        dp={}
        def dfs(i): #O(n)
            if i==n:
                return 0#base case
            if i in dp:
                return dp[i]
            #not take
            res=1+dfs(i+1)
            for j in range(i,n): #O(n)
                if s[i:j+1] in words: #O(n)
                    #take 
                    res=min(res,dfs(j+1))
            dp[i]=res
            return dp[i]

        return dfs(0) #O(n^3)
        
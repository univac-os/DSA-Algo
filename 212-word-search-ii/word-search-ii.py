class TrieNode:
    def __init__(self):
        self.nodes={}
        self.is_end=False

    def addWord(self,word):
        curr=self
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c]=TrieNode()
            curr=curr.nodes[c]#move inside
        curr.is_end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        similar to word search but here we need to check for all words so Backtracking
        but if 2 words have same prefix say app apl for apl we need to search again a-p-l
        we need prefix trie and based on this we will backtrack on board
        """
        m,n=len(board),len(board[0])
        root=TrieNode()
        for w in words:
            root.addWord(w)
        
        res,visit=set(),set()
        def backtrack(r,c,root,w):
            if r<0 or r==m or c<0 or c==n or (r,c) in visit or board[r][c] not in root.nodes:return
            visit.add((r,c))
            root=root.nodes[board[r][c]]
            w+=board[r][c]
            if root.is_end:
                res.add(w)
            #4 dir
            backtrack(r+1,c,root,w)
            backtrack(r-1,c,root,w)
            backtrack(r,c+1,root,w)
            backtrack(r,c-1,root,w)
            visit.remove((r,c))
        
            
        

        for r in range(m):
            for c in range(n):
                backtrack(r,c,root,"")
        return list(res)
class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:
    """
    Trie looks so O(n)
    """
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.end=True #finally end point

    def search(self, word: str) -> bool:
        """
        if we have .ab for . we need to search all the finding and backtrack it
        """
        def dfs(idx,node):
            curr=node
            for i in range(idx,len(word)):
                if word[i]=='.':
                    #check with all children
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr=curr.children[word[i]]

            return curr.end
        
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
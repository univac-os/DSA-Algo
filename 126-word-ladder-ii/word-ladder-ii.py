class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        ties but its long method
        so wildcard pattern can be used here we want all the combination
        so bfs and create a graph and backtracking to get all 
        """
        if endWord not in wordList: return []
        if beginWord==endWord:return [beginWord]
        #1.create a pattern
        pattern=defaultdict(list)
        wordList.append(beginWord)
        wordList=set(wordList)
        for w in wordList:
            for i in range(len(w)):
                pat=w[:i]+"*"+w[i+1:]
                pattern[pat].append(w)

        #2.BFS 
        parent=defaultdict(list)
        level=0
        q=deque([beginWord])
        found=False
        curr_lev={beginWord:0}
        while q and not found:
            level+=1
            for _ in range(len(q)):
                word=q.popleft()
                for i in range(len(word)):
                    pat=word[:i]+"*"+word[i+1:]
                    for nei in pattern[pat]:
                        if nei not in curr_lev:
                            #new node
                            curr_lev[nei]=level
                            parent[nei].append(word) #parent of nei is word
                            q.append(nei)
                        else:
                            # nei in same level so we can get other shortest path
                            if curr_lev[nei]==level:
                                parent[nei].append(word)
                                #no need to add to queue 

                        if nei==endWord:
                            found=True
        #3. Backtracking 
        res=[]
        path=[endWord]

        def dfs(word,path):
            if word == beginWord:
                    res.append(path[::-1]) #begin-->end
                    return 
            
            for p in parent[word]:
                path.append(p)
                dfs(p,path)
                path.pop()
        
        dfs(endWord,[endWord])
        return res
                        


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        ties but its long method
        so wildcard pattern can be used here we want all the combination
        so bfs and create a graph and backtracking to get all 
        we need shortest so who comes first out of queue it is shortest
        """
        if endWord not in wordList: return []
        if beginWord==endWord :return [beginWord]
        wordList.append(beginWord)
        wordList=set(wordList)
        #pattern
        pattern=defaultdict(list)
        n=len(beginWord)
        for w in wordList:
            for i in range(n):
                pat=w[:i]+"*"+w[i+1:]
                pattern[pat].append(w)
        #BFS
        parent=defaultdict(list)
        lev=0
        lev_node={beginWord:0}
        q=deque([beginWord])
        found=False
        while q and not found:
            lev+=1
            for _ in range(len(q)):
                w=q.popleft()
                #check fist time see or on same level we have another option
                for i in range(n):
                    pat=w[:i]+"*"+w[i+1:]
                    for nei in pattern[pat]:
                        if nei not in lev_node:
                            lev_node[nei]=lev
                            parent[nei].append(w)
                            q.append(nei)
                        else:
                            if lev_node[nei]==lev:
                                parent[nei].append(w)
                    
                        if endWord==nei:
                            found=True
                
        #backtracking
        res=[]
        def dfs(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return 
            
            for p in parent[word]:
                path.append(p)
                dfs(p,path)
                path.pop()

        dfs(endWord,[endWord])
        return res
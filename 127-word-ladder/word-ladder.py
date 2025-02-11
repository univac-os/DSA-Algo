class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        difference between char is 1 so ties can used but long method
        so find the pattern and use graph so BFS
        pattern? hit hot pattern here common is h*t so for this pattern we 2 nodes 
        O(n2*m) n is edges to grpah  
        """
        if endWord not in wordList:return 0
        patterns=defaultdict(list)
        wordList=set(wordList)
        wordList.add(beginWord)
        #start from beginword pattern creation and grouping
        for w in wordList:
            for i in range(len(w)):
                pat=w[:i]+"*"+w[i+1:]
                patterns[pat].append(w)
        #we have patterns so start from beginword and based on pattern we will go till endword
        q=deque([beginWord])
        visit=set([beginWord])
        res=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word ==endWord:
                    return res
                #now we have word find each pattern list for this word
                for i in range(len(word)):
                    pat=word[:i]+"*"+word[i+1:]
                    for nW in patterns[pat]:
                        if nW not in visit:
                            visit.add(nW)
                            q.append(nW)
            res+=1
        return 0
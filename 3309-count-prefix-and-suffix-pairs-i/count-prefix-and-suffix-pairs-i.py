class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        #brute force is better? O(n2*k) k is len of word
        res=0
        for i in range(len(words)):
            w1=words[i]
            for j in range(i+1,len(words)):
                w2=words[j]
                if len(w1)>len(w2):
                    continue
                
                if w2.startswith(w1) and w2.endswith(w1):
                    res+=1
        return res
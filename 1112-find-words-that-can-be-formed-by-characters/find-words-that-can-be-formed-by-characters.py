class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=Counter(chars)
        res=0
        for w in words:
            curr_word_hm=defaultdict(int)
            flag=True
            for c in w:
                curr_word_hm[c]+=1
                if c not in count or curr_word_hm[c]>count[c]:
                    flag=False
                    break
            if flag:
                res+=len(w)
        
        return res
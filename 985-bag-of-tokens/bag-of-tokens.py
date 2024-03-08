class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #increase score with small power value and 
        #increase power with more power value 
        #so sort and take from left and right
        res=scrore=0
        tokens.sort()
        l,r=0,len(tokens)-1
        while l<=r:
            if power>=tokens[l]:
                #take it 
                power-=tokens[l]
                l+=1
                scrore+=1
                res=max(res,scrore)
            elif scrore>0:
                #leave it 
                power+=tokens[r]
                r-=1
                scrore-=1
            else:
                break 
        
        return res
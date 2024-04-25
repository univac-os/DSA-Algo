class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #2 times iterate
        #first time add all if any extra (
        #second time remove ( from back ? -- say at (()x)yz( if you remove 1st one ()x)yz( which not right
        res=[]
        cnt=0#extra (
        for c in s:
            if c=='(':
                res.append(c)
                cnt+=1
            elif c==')' and cnt>0:
                #we have pair for it
                res.append(c)
                cnt-=1 #remove the pair
            elif c!=')':
                #normal characters
                res.append(c)
        #second iterator to remove extra (
        filtered=[]
        for c in res[::-1]:
            if cnt >0 and c=='(':
                cnt-=1
            else:
                filtered.append(c)
        
        return ''.join(filtered[::-1])


        
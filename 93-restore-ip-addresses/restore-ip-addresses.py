class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return res
        def backTrack(i,dots,currIP):
            if dots==4 and i==len(s):
                res.append(currIP[:-1])#last we have . so it like x.y.a.b.
                return 
            if dots>4:
                return
            
            for j in range(i,min(i+3,len(s))):
                #take 1 or 2 or 3 so form tree
                #1.check less than 256 
                #2. leading not 0
                if int(s[i:j+1]) <256 and (i==j or s[i]!="0") :
                    backTrack(j+1,dots+1,currIP + s[i:j+1]+".")
        
        backTrack(0,0,"")
        return res
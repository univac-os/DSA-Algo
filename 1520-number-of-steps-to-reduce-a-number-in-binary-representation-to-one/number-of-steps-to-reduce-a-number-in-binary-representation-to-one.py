class Solution:
    def numSteps(self, s: str) -> int:
        def AddOne(s):
            #case 1000111-->1001000
            #111--> 1000
            #so 1 become 0 and first 0 from last become 1 and stop--I
            #if all are 1 then add 1 and remaining are 0 ---II
            idx=len(s)-1
            s=list(s)
            while idx>=0 and s[idx]=="1":
                #replace them with 0 and move
                s[idx]="0"
                idx-=1
            #check I and II
            if idx== -1:#II
                s=["1"]+s 
            else :
                s[idx]="1"
            return "".join(s)

        res=0
        while s!="1":
            if s[-1]=="0":
                #ignore at element
                s=s[:-1]
            else:
                s=AddOne(s)
            res+=1
        return res
        
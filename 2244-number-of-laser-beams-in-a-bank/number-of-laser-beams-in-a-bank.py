class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        looks like math m*n
        """
        prev,res=0,0
        for b in bank:
            cnt=0
            for s in b:
                if s =="1":
                    cnt+=1
            if cnt:
                res+=(prev*cnt)
                prev=cnt #to next so update prev
        return res
                
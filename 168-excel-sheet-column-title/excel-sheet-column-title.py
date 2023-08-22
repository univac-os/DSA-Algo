class Solution:
    def convertToTitle(self, col: int) -> str:
        #base of 26 but here start from 0 ..26 so we need start from 1 ...26
        res=""
        while col>0:
            offset=(col-1)%26#a=0 b=1...z=25
            res+=chr(ord('A')+offset)
            col=(col-1)//26
        
        return res[::-1]#reverse
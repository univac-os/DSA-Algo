class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        OBSERVATION 
        middle bit is alway 1 ,first bit is 0 and last bit is 1
        so  1st half we will same as n-1 value and 2nd half is reverse of 1st half value
        we need to know where k is present,based on this we will give 0/1 as output
        123 4 567--position of digit
        011 1 001 
        abc   cba so k is 5 so we want total len is 7 so 7-5 =2 so from start +2=1+2 =3
        so 3rd pos is 1 and we want reverse of it so 0
        """
        def helper(length,k):
            if length==1:
                return "0"
            #find where k is present n=15 half=7 0..7 8 9..15
            half=length//2
            if k<=half:#1st half
                return helper(half,k)
            elif k>half+1:
                res=helper(half,1+length-k ) #start+ diff from end
                return "0" if res=="1" else "1"
            else:
                return "1"#middle bit
        return helper(2**n-1,k)
        
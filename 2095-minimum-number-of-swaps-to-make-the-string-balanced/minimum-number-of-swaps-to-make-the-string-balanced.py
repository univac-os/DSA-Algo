class Solution:
    def minSwaps(self, s: str) -> int:
        #we need pair [ ] but here we need min swap
        #given that there will be n/2--> [ , n/2 ->],So if we need max[ at any point there will be ] and end to make a pair
        close,maxClose=0,0
        for n in s:
            if n=='[':
                close-=1
            else:
                close+=1
            maxClose=max(maxClose,close)
        #we got at some point we have max ] that need pair so we can use [ from end 
        return (maxClose)//2+ maxClose%2
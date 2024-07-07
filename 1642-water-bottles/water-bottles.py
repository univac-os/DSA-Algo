class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #// -->next drink
        #% add to empty O(logn)
        res=0
        empty=0
        while numBottles>0:
            res+=numBottles
            empty+=numBottles
            #next round
            numBottles=empty//numExchange
            #we want prev round extra bottles
            empty=empty%numExchange
        return res
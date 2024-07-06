class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #check the arrows  t=5 n =4 5//3 =1(odd)  so 2 more from back
        #t=8 n=4 8//3 =2 (even) so remaining 1 from front
        total_round=time//(n-1)
        extra=time%(n-1)

        if total_round%2:
            #odd so back
            return n-extra
        return extra+1
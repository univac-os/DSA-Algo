class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #greedy have more no of change 
        five,ten=0,0
        for b in bills:
            if b ==5:
                five+=1
            if b==10:
                ten+=1
            #we dont need to have count of 20 as there is no higher amount that 20
            #so we dont need to give change of 20
            change=b-5
            if change ==5:
                if five>0:
                    five-=1
                else: return False
            elif change==15:#20
                if five and ten:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else: return False

        return True

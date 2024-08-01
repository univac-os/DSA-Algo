class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        #we want either top or bottom should have same value
        #take the 1st element from top and bottom and check for that
        for target in [tops[0],bottoms[0]]:
            missTop,missBottom=0,0
            for idx,pair in enumerate(zip(tops,bottoms)):
                top,bottom=pair
                #check any number matches with top or bottom
                if not (top ==target or bottom ==target):
                    break # some other number then we cant get answer
                
                if top!=target: missTop+=1
                if bottom!=target:missBottom+=1

                if idx==len(tops)-1:
                    return min(missTop,missBottom)
        return -1
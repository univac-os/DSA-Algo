class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1]) #descending order
        res=0
        for n,b in boxTypes:
            if truckSize>0:
                res+=(min(n,truckSize)*b)
                truckSize-=n
        return res
            
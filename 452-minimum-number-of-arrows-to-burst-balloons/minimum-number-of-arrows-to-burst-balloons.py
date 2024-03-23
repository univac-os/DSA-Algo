class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #sort by start time
        #check start of prev and end of curr
        #[1,5] [2,7] -->[2,5] or max(starts),min(ends)
        #[1,5]  [2,4] -->[2,4] so max(starts) is 2nd elements as its sorted
        points.sort()
        prev=points[0]
        res=len(points)
        for i in range(1,len(points)):
            curr=points[i]
            #check
            if curr[0]<=prev[-1]:#check start and end 
                res-=1
                prev=[curr[0],min(prev[-1],curr[-1])]
            else:
                prev=curr

        return res

        
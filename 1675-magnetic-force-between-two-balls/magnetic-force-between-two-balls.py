class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #we need max from all mini 
        #check distance and move binaray search
        def canFind(req_dist):
            balls=1
            prev_idx=position[0]
            for b in position:
                if b- prev_idx>=req_dist:
                    balls+=1
                    prev_idx=b
            return balls>=m

        
        position.sort()
        l=1
        r=position[-1]-position[0] #we will search from start to end 
        while l<r:
            mid=(l+r+1)//2
            if canFind(mid):
                #we got a value GREEDY we need maxi
                l=mid
            else:
                r=mid-1
        return l
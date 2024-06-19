class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #binary search from min to max on array O(logn*n)
        def canPossible(mid):
            count=0
            ans=0
            for d in bloomDay:
                if d<=mid:
                    count+=1
                else:
                    ans+=count//k
                    count=0
            ans+=count//k
            return ans>=m
        
        if m*k>len(bloomDay):
            return -1
        
        l=min(bloomDay)
        r=max(bloomDay)
        while (l<=r):
            mid=(l+r)//2
            if canPossible(mid):
                #got a value GREEDY check less
                r=mid-1
                
            else:
                l=mid+1
        return l
        
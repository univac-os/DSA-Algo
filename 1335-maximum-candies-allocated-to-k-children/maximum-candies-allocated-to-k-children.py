class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        take example 2,7 and k =4 so sum is 9 and 9/4 = 2 so 2 can be answer
        7=2+2+2+1 if k=5 9/5 is 1 
        so we need to check whether 1 can answer ,can we break 2 and 7 yes
        5,8,6 and k=3 sum is 19 so 19/3 is 6 can 6 be answer NO beacuse 5 cant divide into 6
        so answer will be from 1 to 6 check say 3 yes ,4 yes ,5 yes
        SO Binary search 
        """
        total=sum(candies)
        if total<k:return 0
        l,r=1,total//k
        res=0
        while l<=r:
            m=(l+r)//2
            count=0
            for c in candies:
                if c//m:
                    count+=c//m
                if count>=k:
                    break
            
            if count>=k:
                #greedy find max
                res=m
                l=m+1
            else:
                r=m-1
        return res
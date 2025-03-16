class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        r and n are variable here
        looking at example we want mini time all will be done so working in parallel so 
        r*n2=time here  r1*n1^2  <=time r2*n2^2 <=time ...
        so looking at say we now r1 ,r2.. are constant n is variable so n=sqrt(time/r)
        now we can find the n if we add all n1,n2... and if n1,n2..>N so we reduce time and check it
        so BINARY SEARCH
        """
        def can_repair(time):
            count=0
            for r in ranks:
                count+=int(sqrt(time/r))
            return count>=cars

        l,r=1,min(ranks)*cars*cars
        res=0
        while l<=r:
            m=(l+r)//2
            if can_repair(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
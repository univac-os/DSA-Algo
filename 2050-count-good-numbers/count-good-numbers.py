class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        general power gives time limit exceeded
        so 5**even is O(even) so make it log 
        """
        even=ceil(n/2)
        odd=n-even
        mod=10**9+7
        def pow(x,n):
            res=1
            while n>0:
                if n%2:
                    res=(res*x)%mod
                n=n//2
                x=(x*x)%mod
            return res
        
        return (pow(5,even)*pow(4,odd))%mod

        return ((5**even %mod)*(4**odd%mod))%mod
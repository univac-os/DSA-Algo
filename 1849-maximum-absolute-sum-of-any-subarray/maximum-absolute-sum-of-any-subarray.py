class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        kadane algo type but here we want abs
        prefix sum  num
        +             +. inceases
        +.           -    deceases
        -            +.  decrease
        -            -    increase
        so we want min and max prefix at num
        """
        curr=0
        maxi,mini=0,0
        res=0
        for n in nums:
            curr+=n
            res=max(res,abs(curr-maxi),abs(curr-mini))
            maxi=max(maxi,curr)
            mini=min(mini,curr)
        return res
            
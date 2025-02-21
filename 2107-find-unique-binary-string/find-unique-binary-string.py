class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        combinator 2^n and find the missing one O(n2) as 
        """
        def backtrack(ds):
            if len(ds)==len(nums):
                if ds not in nums:
                    return ds
                return ""
            #2 option 0 or 1
            ds=ds+"0"
            zero=backtrack(ds)
            if zero!="":return zero
            ds=ds[:len(ds)-1]
            ds=ds+"1"
            one=backtrack(ds)
            if one!="":return one
            return ""
        
        nums=set(nums)#search will be O(1)
        return backtrack("")
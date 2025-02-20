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
            zero=backtrack(ds+"0")
            if zero!="":return zero
            
            one=backtrack(ds+"1")
            if one!="":return one
            return ""
        
        nums=set(nums)#search will be O(1)
        return backtrack("")
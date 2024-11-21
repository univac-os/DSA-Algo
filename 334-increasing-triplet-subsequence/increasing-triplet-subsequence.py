class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        thought--> sliding window bt here we want subseq not subarray so NOT A SOLUTION
        so here we want 3 number only 
        """
        i=j=float('inf')
        for n in nums:
            if n>j:
                #means we got 3rd number
                return True
            elif n>i:
                #we got second number so modify j
                j=n
            else:
                #we got first number so modify i
                i=n
        return False
